from keras.models import Model, load_model

import numpy as np
import pandas as pd
import cv2
import os

class Cat_landmarks(object):
    
    """
    @base_path:
        (String) Path for image files you want to extract landmarks 
    
    ----------------- Usage Manual -----------------
    1. Download pre-trained models "bbs_1.h5, lmks_1.h5".
    2. Put them in "models" folder in the same working directory with this module.
    3. After all, You can use it.
    
    ------------------- Optional -------------------
    You can change image size using ".img_size = 000".
    
    """
    
    model_path = 'models'
    
    __bbs_model_name = os.path.join(model_path, 'bbs_1.h5')
    __lmks_model_name = os.path.join(model_path, 'lmks_1.h5')

    __bbs_model = load_model(__bbs_model_name)
    __lmks_model = load_model(__lmks_model_name)
    
    
    def __init__(self, base_path):
        self.base_path = base_path
        self.file_list = sorted(os.listdir(self.base_path))
        self.img_size = 224
        
    def extract_landmarks(self, position='all', extract_face=False):
        """
        @position:
            
            Input below strings.
            You can choose below options.
            
            1. "left_eye"
            2. "right_eye"
            3. "nose"
            4. "left_ear"
            5. "right_ear"
            6. "all"
        
        @extract_face:
            
            If you want to extract face image,
            input "extract_face=True".
            
        """
        for f in self.file_list:
            if ('jpg' not in f) and ('jpeg' not in f) and ('png' not in f):
                continue

            img = cv2.imread(os.path.join(self.base_path, f))
            ori_img = img.copy()
            result_img = img.copy()

            # predict bounding box
            img, ratio, top, left = self.__resize_img(img)

            inputs = (img.astype('float32') / 255).reshape((1, self.img_size, self.img_size, 3))
            pred_bb = self.__bbs_model.predict(inputs)[0].reshape((-1, 2))

            # compute bounding box of original image
            ori_bb = ((pred_bb - np.array([left, top])) / ratio).astype(np.int)

            # compute lazy bounding box for detecting landmarks
            center = np.mean(ori_bb, axis=0)
            face_size = max(np.abs(ori_bb[1] - ori_bb[0]))
            new_bb = np.array([
                center - face_size * 0.7,
                center + face_size * 0.7
            ]).astype(np.int)
            new_bb = np.clip(new_bb, 0, 99999)

            # predict landmarks
            face_img = ori_img[new_bb[0][1]:new_bb[1][1], new_bb[0][0]:new_bb[1][0]]
            face_img2, face_ratio, face_top, face_left = self.__resize_img(face_img)

            face_inputs = (face_img2.astype('float32') / 255).reshape((1, self.img_size, self.img_size, 3))

            pred_lmks = self.__lmks_model.predict(face_inputs)[0].reshape((-1, 2))

            # compute landmark of original image
            new_lmks = ((pred_lmks - np.array([face_left, face_top])) / face_ratio).astype(np.int)
            ori_lmks = new_lmks + new_bb[0]
            
            self.__extraction(f, face_img, ori_img, ori_lmks, face_size, position)
            
            if extract_face:
                filename, ext = os.path.splitext(f)
                cv2.imwrite('{}/{}_face_{}'.format(position, filename, ext), face_img)
            
    def __resize_img(self, img):
        old_size = img.shape[:2] # old_size is in (height, width) format
        ratio = float(self.img_size) / max(old_size)        
        new_size = tuple([int(x*ratio) for x in old_size])
        
        # new_size should be in (width, height) format
        img = cv2.resize(img, (new_size[1], new_size[0]))
        
        delta_w = self.img_size - new_size[1]
        delta_h = self.img_size - new_size[0]
        
        top, bottom = delta_h // 2, delta_h - (delta_h // 2)
        left, right = delta_w // 2, delta_w - (delta_w // 2)
        
        new_img = cv2.copyMakeBorder(img, top, bottom, left, right, 
                                     cv2.BORDER_CONSTANT, value=[0, 0, 0])
        
        return new_img, ratio, top, left
    
    def __extraction(self, f, face_img, ori_img, ori_lmks, face_size, position):
        
        def find_landmarks():

            if i < 2:
                ratio = 0.12
            elif i == 2:
                ratio = 0.15
            else:
                ratio= 0.05

            if i <= 2:

                l = ori_lmks[i]

                bbl = np.array([
                    l - face_size * ratio,
                    l + face_size * ratio
                ]).astype(np.int)
                bbl = np.clip(bbl, 0, 99999)

            else:

                idx = 3 * (i-2)
                l = ori_lmks[idx:idx+3]

                bbl = np.array([
                    np.min(l, axis=0) - face_size * ratio,
                    np.max(l, axis=0) + face_size * ratio
                ]).astype(np.int)
                bbl = np.clip(bbl, 0, 99999)

            # cv2.rectangle(ori_img, pt1=tuple(bbl[0]), pt2=tuple(bbl[1]), color=(255, 255, 255), thickness=2)

            lmks_img = ori_img[bbl[0][1]:bbl[1][1], bbl[0][0]:bbl[1][0]]
            filename, ext = os.path.splitext(f)

            # cv2.imwrite('lmks_imgs/{}_bbs{}'.format(filename, ext), ori_img)
            
            path = os.path.join('lmks_imgs', position)
            if not os.path.exists(path):
                os.makedirs(path)

            if position == 'all':
                cv2.imwrite('lmks_imgs/{0}/{1}_{0}_0{2}{3}'.format(position, filename, i+1, ext), lmks_img)
            else:
                cv2.imwrite('lmks_imgs/{0}/{1}_{0}{2}'.format(position, filename, ext), lmks_img)
    

        # try:

        if position == 'all':

            for i in range(5):

                find_landmarks()
        
        else:
            
            if position == 'left_eye':
                i = 0

            elif position == 'right_eye':
                i = 1

            elif position == 'nose':
                i = 2

            elif position == 'left_ear':
                i = 3

            elif position == 'right_ear':
                i = 4
            
            find_landmarks()

        # except:

            # raise ValueError("position is not correct, you must select position in ( 'all', 'left_eye', 'right_eye', 'left_ear', 'right_ear' ).")