import os

folder = "Dataset/Training"

total = 0

for letter in os.listdir(folder):

    path = os.path.join(folder, letter)

    if os.path.isdir(path):

        count = len(os.listdir(path))

        print(letter, ":", count)

        total += count

print("\nTotal images:", total)