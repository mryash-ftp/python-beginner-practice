nums = [1,2,2,3,4,4,5]

unique = []
for i in nums:
    if i in unique:
        pass
    else:
        unique.append(i)
        
print(unique)

# Output: [1,2,3,4,5]
