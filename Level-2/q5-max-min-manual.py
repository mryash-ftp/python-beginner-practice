# Level 2 Question 5:
# Find max/min from 5 numbers WITHOUT using max() or min()
numbers = list(map(int, input("Enter 5 numbers: ").split()))
max_val = numbers[0]
min_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("Max:", max_val, "Min:", min_val)