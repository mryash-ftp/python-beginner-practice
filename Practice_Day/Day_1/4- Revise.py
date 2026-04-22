n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("FizzBuzz",n)
elif n%3==0:
    print("Fizz",n)
elif n%5==0:
    print("Buzz",n)