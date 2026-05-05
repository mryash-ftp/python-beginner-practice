import json

def datafeed():
    with open("data1.json","r") as f:
        old_data = json.load(f)
        print(old_data)
    name=input("Enter your name: ")
    mob=input("Enter your mobile: ")
    dob=input("Enter DOB(DD/MM/YYYY):" )
    code=input("Enter your language_coding(c++,c#,c,python): ")
    data={
        "name":name,
        "mobile":mob,
        "dob":dob,
        "code":code
        }
    
    old_data.append(data)

    with open("data1.json","w") as f:
        json.dump(old_data,f,indent=4)

    print("Student Data Saved")

def access():
    name=input("Enter your name: ").lower()
    with open("data1.json","r") as f:
        old_data = json.load(f)
        for index,i in enumerate(old_data):
           if name==old_data[index]["name"].lower():
            print("Name:",old_data[index]['name'])
            print("Mobile No:",old_data[index]['mobile'])
            print("DOB:",old_data[index]['dob'])
            print("Code Language:",old_data[index]['code'])
            break
        else:
           print("data not found")

datafeed()
access()
