# Level 1 Question 8:
# Take a number N from the user and print the sum of 1 to N.
n = int(input("Enter a number: "))
temp = 0
for i in range(1, n + 1):
    temp += i
print("Sum:", temp)