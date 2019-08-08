import random
import cv2, os
import pandas as pd
import numpy as np

dirname = 'CAT_00'
base_path = 'C:/Users/Jwp/Desktop/workspace/python/ML_Tools/dataset/Cat_Hipsterizer/%s' % dirname
file_lists = sorted(os.listdir(base_path))

for f in file_lists:
    if '.cat' not in f:
        continue

    # read landmarks
    pd_frame = pd.read_csv(os.path.join(base_path, f), sep=' ', header=None)
    landmarks = (pd_frame.values[0][1:-1]).reshape((-1, 2)).astype(np.int)

    # load image
    img_filename, ext = os.path.splitext(f)

    img = cv2.imread(os.path.join(base_path, img_filename))

    # visualize
    for landmark in landmarks:
        cv2.circle(img, center=tuple(landmark), radius=1, color=(0, 0, 255), thickness=2)

    cv2.imshow('img', img)
    if cv2.waitKey(0) == ord('q'):
        break
    
    break