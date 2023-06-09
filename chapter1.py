from cv2 import cv2

# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# img = cv2.imread("Resources/roy.jpg")
#
# cv2.imshow("Picture", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/Paralax 1 - Alexandre Chambon.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
#

cap = cv2.VideoCapture(0)
cap.set(10,80)

while True:
    success, img = cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
