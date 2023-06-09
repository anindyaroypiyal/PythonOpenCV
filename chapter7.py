import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min", "TrackBars", 0,179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 173,179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 46,255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255,255, empty)
cv2.createTrackbar("Val min", "TrackBars", 109,255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255,255, empty)
# cv2.createTrackbar("hh", "TrackBars", 123, 321, empty)

while True:
    img1 = cv2.imread("Resources/car yellow.jpg")
    imgHSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    # s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    s_max = 255
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img1, img1, mask=mask)

    cv2.imshow("original", img1)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Masked image",mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)