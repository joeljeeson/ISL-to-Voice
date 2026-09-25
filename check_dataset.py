# this is used to see what's inside the letters folder
import os

folder = "Dataset/Letters"

for image in os.listdir(folder):
    print(image)



#lets see what's inside the training folder
for i in os.listdir("Dataset/Training"):
    print(i)
