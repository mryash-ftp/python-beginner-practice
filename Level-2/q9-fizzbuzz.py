# Level 2 Question 9:
# FizzBuzz: 1-50 (3=Fizz, 5=Buzz, 15=FizzBuzz)
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)