import json

name=input("Enter Your Name:")
Class=input("Enter Your Class:")
dob=input("Enter Your Class(DD/MM/YYYY):")
subject=input("Enter Your Subject:")
mob=int(input("Enter Your Mobile Number:"))

student ={

    "name": name,
    "class":Class,
    "dob":dob,
    "subject":subject,
    "mobile":mob
}
with open("Student_data.json","w") as f:
    json.dump(student,f,indent=4)

print("Student Data Saved")
