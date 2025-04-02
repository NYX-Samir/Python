import os

folder_path = r"C:\Users\evilk\Downloads\PNG"
files = os.listdir(folder_path)

for file in files:
    print(file)
