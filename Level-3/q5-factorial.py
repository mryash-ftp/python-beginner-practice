# q5-factorial.py
def facto(n):
    b = 1
    for i in range(1, n + 1):
        b *= i
    return b

print(facto(5))