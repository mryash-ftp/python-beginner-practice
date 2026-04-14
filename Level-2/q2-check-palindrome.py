# Level 2 Question 2:
# Check if a word is palindrome (same forward/backward)
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("Palindrome!")
else:
    print("Not Palindrome")