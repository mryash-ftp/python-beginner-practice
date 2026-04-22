n=int(input("Enter a number: "))
for i in range(1,int(n**0.5)+1):
    a=i**2
    if a==n:
        print("Perfect square")
        break
else:
     print("Not a perfect square")
