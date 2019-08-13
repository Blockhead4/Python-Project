import cv2

img_color = cv2.imread('box.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
img_sobel_y = cv2.convertScaleAbs(img_sobel_y)


img_sobel = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0);


cv2.imshow("Sobel X", img_sobel_x)
cv2.imshow("Sobel Y", img_sobel_y)
cv2.imshow("Sobel", img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()