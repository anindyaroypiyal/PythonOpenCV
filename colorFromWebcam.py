import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min", "TrackBars", 24,179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 85,179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 94,255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255,255, empty)
cv2.createTrackbar("Val min", "TrackBars", 71,255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255,255, empty)

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,80)

while True:
    # img1 = cv2.imread("Resources/car yellow.jpg")
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)


    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # lower = np.array([24, 85, 94])
    # upper = np.array([71, 255, 255])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

    cv2.imshow("original", img)
    # cv2.imshow("HSV", imgHSV)
    cv2.imshow("Masked image",mask)
    cv2.imshow("Result", imgResult)
    # cv2.waitKey(1)