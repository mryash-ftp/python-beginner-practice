# q9-palindrome.py
def palindrome(a):
    if a == a[::-1]:
        return "Its Palindrome"
    else:
        return "Not Palindrome"

name = "Mam".lower()
print(palindrome(name))