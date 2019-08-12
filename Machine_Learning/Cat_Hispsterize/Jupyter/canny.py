import cv2
import numpy as np
import argparse
import glob

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.max(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    print('lower: %d  upper: %d' % (lower, upper))

    # return the edged image
    return edged


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--lmks_imgs", required=True, help="path to input dataset of images")
args = vars(ap.parse_args())
#canny.py -i image
# loop over the images

i = 0
for imagePath in glob.glob(args["lmks_imgs"] + "/*.jpg"):

    if i == 2:
        # load the image, convert it to grayscale, and blur it slightly
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        kernel = np.ones((5,5), np.float32)/25
        blur = cv2.filter2D(image, -1, kernel)

        # apply Canny edge detection using a wide threshold, tight
        # threshold, and automatically determined threshold
        wide = cv2.Canny(blur, 20, 255)
        # tight = cv2.Canny(blur, 225, 250)
        # auto = auto_canny(blur, 0)

        # show the images
        # cv2.imshow("Original", image)
        # cv2.imshow("Edges", np.hstack([wide, tight, auto]))
        # cv2.imshow("wide, tight", np.hstack([wide, tight]))
        cv2.imshow("wide", wide)
        # cv2.imshow("tight", tight)
        # cv2.imshow("Edges", auto)

        # cv2.imwrite('canny_imgs/00{}_wide.jpg'.format(i), wide)
        cv2.waitKey(0)
        
        break
    
    i += 1


# src = cv2.imread("canny_imgs/002_auto.jpg", cv2.IMREAD_COLOR)
# x,y,z = src.shape

# kernel = np.ones((5,5), np.float32)/25
# blur = cv2.filter2D(src, -1, kernel)


# canny = cv2.Canny(src, 127, 255)
# canny_blur = cv2.Canny(blur, 127, 255)
# dim= np.zeros((x,y))
# canny = np.dstack((canny,dim,dim))
# canny_blur = np.dstack((canny_blur,dim,dim))

# for i in range(len(canny)):
#  	for j in range(canny.shape[1]):
#  		if (canny[i][j][0] == 255):
#  			canny[i][j][1], canny[i][j][2]=255,255

# for i in range(len(canny_blur)):
#  	for j in range(canny_blur.shape[1]):
#  		if (canny_blur[i][j][0] == 255):
#  			canny_blur[i][j][1], canny_blur[i][j][2]=255,255
			
# result = np.where(canny == 255)
# result = [(i,v) for i,v in zip(result[0],result[1])]


# cv2.imshow("canny", canny)
# cv2.imshow("canny_blur", canny_blur)
# cv2.imshow("ORIGN", src)
# cv2.imshow("canny, canny_blur",np.hstack((canny, canny_blur)))

# cv2.imshow("sobel", sobel)
# cv2.imshow("laplacian", laplacian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()