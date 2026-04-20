import json
import os

FILE_NAME = "Student_data.json"

def save_student():
    # 1. Inputs lena
    name = input("Enter Name: ")
    mob = input("Enter Mobile: ")
    student_info = {"name": name, "mobile": mob}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = f.read()
            if data == "": 
                all_students = []
            else:
                all_students = json.loads(data)
    else:
        all_students = []

    all_students.append(student_info)


    with open(FILE_NAME, "w") as f:
        json.dump(all_students, f, indent=4)
    
    print("✅ Student Data Saved Successfully!")

# Program Start
save_student()
