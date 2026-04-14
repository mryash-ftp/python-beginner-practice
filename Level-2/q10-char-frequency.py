# Level 2 Question 10:
# Count frequency of each character using dictionary
text = input("Enter text: ").lower()
freq = {}
for char in text:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1
print("Character frequency:")
for char, count in freq.items():
    print(f"{char}: {count}")