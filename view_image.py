import cv2

image = cv2.imread("Dataset/Training/A/0.jpg")

print("Original:", image.shape)

image = cv2.resize(image, (128, 128))

print("After resize:", image.shape)

cv2.imshow("ISL Image", image)

while True:
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
