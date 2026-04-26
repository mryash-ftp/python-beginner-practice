import datetime as dt

def utility():
    a=dt.datetime.now()
    print(a.strftime("Date: %d-%m-%y | Time : %I:%H:%S"))
    if a.year%4==0 or a.year%100==0 and a.year%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
def converter(c) :
    f=c*(9/5+32)
    print("Fahrenheit",f)
def Asci(n):
    if n.isalpha():
        print("ASCII Value Of",n,":",ord(n))
    else:
        print("Enter only letters")
user=input("Enter a number: ")  
utility()
converter(10)
Asci(user)
