import cv2

image = cv2.imread("ISL/Dataset/Training/A/0.jpg")

cv2.imshow("ISL Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows