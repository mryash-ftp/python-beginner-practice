items = [('pen', 10), ('book', 50), ('copy', 20)]
for index, item in enumerate(items):
    print(index, item[0], index*item[1])
    a += index*item[1]
print("Grand Total:", a)
