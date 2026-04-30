import os

path = "C:\\Data_File"

os.makedirs(path, exist_ok=True)

file = os.path.join(path, "Data.txt")

with open(file, "a") as f:
    f.write("Hello " + "\n")

print("Folder and file created successfully!")

