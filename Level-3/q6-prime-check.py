# q6-prime-check.py
def prime_check(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(prime_check(7))