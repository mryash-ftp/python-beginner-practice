import os

class MyFileManager:
    def __init__(self, folder_path):
        self.path = folder_path

    def show_files(self):
        # Folder ke andar ki files ki list nikalna
        try:
            files = os.listdir(self.path)
            print(f"Files in {self.path}:")
            for f in files:
                print(f"- {f}")
        except FileNotFoundError:
            print("Bhai, ye folder toh hai hi nahi!")

# Use kaise karein:
# Aap apne kisi bhi folder ka path yahan daal sakte hain
manager = MyFileManager("C:/Users/Documents") 
manager.show_files()
