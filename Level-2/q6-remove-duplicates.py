# Level 2 Question 6:
# Remove duplicates from list while keeping order
nums = [1, 2, 2, 3, 1, 4, 4]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("Original:", nums)
print("Unique:", unique)