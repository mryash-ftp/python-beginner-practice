# q7-fibonacci.py
def fibo(x):
    a, b = 0, 1
    result = []
    for _ in range(x):
        result.append(a)
        a, b = b, a + b
    return result

print(fibo(5))