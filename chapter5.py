import numpy as np
import cv2

img = cv2.imread("Resources/Perspective Crop 1 - Adrienguh.jpg")
width, height = 300,400
print(img.shape)
pts1 = np.float32([[425,146],[732,166], [421,650], [727,624]])
pts2 = np.float32([[0,0],[width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgPersp = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("source image", img)
cv2.imshow("perspective", imgPersp)
print(imgPersp.shape)
cv2.waitKey(0)