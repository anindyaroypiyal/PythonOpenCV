import cv2
import numpy as np
frameWidth = 300
frameHeight = 300
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 80)

myColors = [[24, 94, 71, 85, 255, 255],
            [42,71,50,160,255,255],
            [42,90,50,156,255,255],
            [44,110,36,179,255,255],
            [70,99,36,179,205,255]]

myColorValues = [[51,153,255],
                 [255,0,255],           #BGR
                 [0,255,0],
                 [255,255,0],
                 [255,0,150]]

myPoints = []   #[x, y, colorId]

def detColors(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for clr in myColors:
        lower = np.array(clr[0:3])
        upper = np.array(clr[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(img1, (x,y), 10, myColorValues[count], cv2.FILLED)
        # imgResult = cv2.bitwise_and(img, img, mask=mask)
        if x!= 0 and y!=0:
            newPoints.append([x, y, count])
        count = count + 1
        # cv2.imshow(str(clr[0]), imgResult)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(img1,cnt,-1,(50,50,50),2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x , y , w, h = cv2.boundingRect(approx)
    return x+w//2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(img1, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    img1 = img.copy()
    newPoints = detColors(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("webcam", img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
