primes = []

def prime_check(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

primes = [n for n in range(2,20) if prime_check(n)]
print("Q5:", primes)
    


# Output: [2,3,5,7,11,13,17,19]
