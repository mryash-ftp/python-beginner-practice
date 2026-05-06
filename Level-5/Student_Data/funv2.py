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
    name = input("Enter your name: ").lower()

    with open("data1.json", "r") as f:
        old_data = json.load(f)

    found = False
    for entry in old_data:
        if name in map(str.lower, entry.values()):
            for k, v in entry.items():
                print(k,':', v)
                found = True

    if not found:
        print("data not found")

# datafeed()
access()
