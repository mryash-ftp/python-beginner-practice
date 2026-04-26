def calculation(n1,n2):
    print(f"{"-"*40}\nPerforming calculations...\n{"-"*40}")
    return f"Addition of {n1} + {n2} = {n1+n2}\nSubtraction of {n1} - {n2} = {n1-n2}\nMultiplication of {n1} * {n2} = {n1*n2}\nDivision of {n1} / {n2} = {n1/n2}"
  
def even_odd(n1,n2):
    print(f"{"-"*40}\nChecking even and odd...\n{"-"*40}")
    return f"\n{n1} is {'even' if n1%2==0 else 'odd'}\n{n2} is {'even' if n2%2==0 else 'odd'}"


def prime(n1,n2):
    print(f"{"-"*40}\nChecking prime numbers...\n{"-"*40}")
    list=[n1,n2]
    for i in list:
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    print(f"{i} is not a prime number")
                    break
            else:
                print(f"{i} is a prime number")
        else:
            return f"{i} is not a prime number"
    return f"{"-"*40}"

def facto():
    print(f"{"-"*40}\nCalculating factorial...\n{"-"*40}")
    List=[n1,n2]
    for i in List:
        fact=1
        for j in range(1,i+1):
            fact*=j
        return f"Factorial of {i} is {fact}"
    return f"{"-"*40}"
def fibo():
    a,b=0,1
    print(f"{"-"*40}Fibonacci series up to {n1} and {n2}:{"-"*40}")
    list=[n1,n2]
    for i in list:
        for j in range(i):
            a,b=0,1
            for _ in range(j):
                print(a,end=' ')
                a,b=b,a+b
    return f"{"-"*40}"
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print(calculation(n1,n2))
print(even_odd(n1,n2))
print(prime(n1,n2))
print(facto())
print(fibo())
