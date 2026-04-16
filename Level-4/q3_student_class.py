class Student :
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def show(self):
        print("Name",self.name)
        print("Roll No:",self.roll_no)
        print("Marks:",self.marks)
    def result(self):
        if self.marks>=33:
            print("Result:","Pass")
        else:
            print("Result:","Fail")
v=Student("Alven","AB8972SX",75)
v.show()
v.result()
