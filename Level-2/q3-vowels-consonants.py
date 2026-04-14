# Level 2 Question 3:
# Count vowels and consonants in a string (ignore spaces/symbols)
text = input("Enter text: ").lower()
vowels = 0
consonants = 0
for char in text:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")