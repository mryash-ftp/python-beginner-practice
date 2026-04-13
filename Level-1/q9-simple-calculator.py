# Level 1 Question 9:
# Make a simple menu-based calculator for 2 numbers.
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = int(input("Enter: [1] Add [2] Subtract [3] Multiply [4] Divide : "))
if op == 1:
    print("Add:", a + b)
elif op == 2:
    print("Subtract:", a - b)
elif op == 3:
    print("Multiply:", a * b)
elif op == 4:
    print("Division:", a / b)
else:
    print("Invalid choice")