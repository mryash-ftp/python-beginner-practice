import json
user_input = input("Choise\n[]1. Add student data\n2. Search student data\nEnter your choice: ")
if user_input == "1":
    with open('Student_data.json', 'r') as file:
        data = json.load(file)
        old_data = data
    with open('Student_data.json', 'w') as file:
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: "))
        subjects = input("Enter the subjects of the student (comma separated): ").split(",")
        mobile = input("Enter the mobile number of the student: ")

        a=[{ "Name": name, "Age": age, "subjects": subjects, "mobile": mobile }]
        
        old_data.extend(a)

        json.dump(old_data, file, indent=4)
        print("Student data added successfully.")

if user_input == "2":
    name = input("Enter the name of the student: ")
    with open('Student_data.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if name.lower()==i['Name'].lower():
                print(f"{'='*20}\nStudent found\n{'='*20}")
                print(f"Name: {i['Name']}")
                print(f"Age: {i['Age']}")
                print(f"Subjects: {', '.join(i['subjects'])}")
                print(f"Mobile: {i['mobile']}")
                break
            else:
                print("Student not found.")
        