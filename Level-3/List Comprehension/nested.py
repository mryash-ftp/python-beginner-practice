nested = [[1,2,3], [4,5], [6,7,8,9]]
flattened = []

for i in nested:
    flattened.extend(i)
print(flattened)

# Output: [1,2,3,4,5,6,7,8,9]
