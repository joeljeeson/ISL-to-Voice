import cv2
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder

folder = "Dataset/Training"

X = []
y = []

for letter in os.listdir(folder):

    path = os.path.join(folder, letter)

    if os.path.isdir(path):

        for image_name in os.listdir(path):

            image_path = os.path.join(path, image_name)

            image = cv2.imread(image_path)

            if image is not None:

                image = cv2.resize(image, (128, 128))

                X.append(image)
                y.append(letter)


# Convert to NumPy arrays
X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Classes:", np.unique(y))


# Encode letters into numbers
encoder = LabelEncoder()

y = encoder.fit_transform(y)

print("Encoded classes:", np.unique(y))
print("Class names:", encoder.classes_)


# Normalize images
X = X.astype("float32") / 255.0

print("Pixel minimum:", X.min())
print("Pixel maximum:", X.max())