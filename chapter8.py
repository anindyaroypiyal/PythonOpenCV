import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(50,50,50),2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            print(approx)
            x , y , w, h = cv2.boundingRect(approx)

            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor == 5:
                objectType = "Pentagon"
            elif objCor == 6:
                objectType = "Hexagon"
            elif objCor > 6:
                centre = (x+(w//2),y+(h//2))
                print("centre",centre)
                print("WIDTH",w)
                print("height",h)
                # print("x=",centre+w//2)
                # print("Y=",centre+h//2)
                objectType = "Circle"
                # if centre + w == centre + h:
                #     objectType = "Circle"
                # else: objectType = "Ellipse"
            else: objectType = "None"

            cv2.rectangle(imgContour, (x,y), (x+w+3,y+h+3),(0,255,0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                        (255,255,255),1)



path = "Resources/cont_new.png"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgGray, 50 , 50)
imgContour = img.copy()

cv2.imshow("source image",img)
# cv2.imshow("Grayscale",imgGray)
# cv2.imshow("blur image", imgBlur)
cv2.imshow("canny",imgCanny)
getContours(imgCanny)
cv2.imshow("detected", imgContour)


cv2.waitKey(0)