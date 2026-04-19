import json

student ={

    "name":"Alven",
    "class":"B.A",
    "dob":"20/12/2007",
    "subject":"Python",
    "mobile":9795941891,
    
}
with open("Student_data.json","w") as f:
    json.dump(student,f,indent=4)
    
print("Student Data Saved")
