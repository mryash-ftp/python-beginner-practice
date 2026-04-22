string="Python".lower()
vowel_count=0
counsonant_count=0
vowerls="aeiou"
for i in string:
    if i in vowerls:
        vowel_count+=1
    else:
        counsonant_count+=1
print("Number of vowels:", vowel_count)
print("Number of consonants:", counsonant_count)