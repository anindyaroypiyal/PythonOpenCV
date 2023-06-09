import cv2
import numpy
import numpy as np
# there is a stack image function missing which can be found in the website of the tutorial.

img = cv2.imread("Resources/roy (2).jpg")

ImgHor = np.hstack((img,img))
imgVert = np.vstack((img,img))

cv2.imshow("Horizontal Stack", ImgHor)
cv2.imshow("Vertical Stack", imgVert)

cv2.waitKey(0)