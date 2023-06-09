from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/roy (2).jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgGray, 150, 250)
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

#cv2.imshow("real image", img)
cv2.imshow("Grey Image", imgGray)
#cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgErode)

cv2.waitKey(0)