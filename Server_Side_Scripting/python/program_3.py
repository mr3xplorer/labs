import os

path = input("Give path: ")

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    file_size = os.path.getsize(file_path)
    print(file_path, file_size)
