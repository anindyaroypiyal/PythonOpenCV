import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#img[:] = 253, 209, 114
#print(img)
cv2.line(img, (0,512), (256,256), (63, 103, 253), 3)
cv2.rectangle(img, (100,150), (400,290), (220, 227, 40), 2)
cv2.circle(img, (256,256), 50, (40, 227, 220), 4)
cv2.putText(img," SHAPES ", (173,40), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
cv2.imshow("image", img)

cv2.waitKey(0)