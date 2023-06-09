import cv2

img = cv2.imread("Resources/roy (2).jpg")
print(img.shape)

imgResize = cv2.resize(img,(300, 550))

imgCropped = img[100:640,20:420]

cv2.imshow("source image", img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped image", imgCropped)

cv2.waitKey(0)