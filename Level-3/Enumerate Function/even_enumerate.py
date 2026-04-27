numbers = [10, 20, 30, 40, 50]

for index,num in enumerate(numbers):
    if index==0 or index%2==0:
        print(f"{index} : {num}")
