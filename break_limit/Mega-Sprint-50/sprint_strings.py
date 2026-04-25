def analysis(user):
    count=0
    for i in user.lower():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
    print(f"Number of vowels in the sentence: {count}")
    uppcount=0
    lowcount=0
    for i in user:
        if i.isupper():
            uppcount+=1
        elif i.islower():
            lowcount+=1

    print(f"Number of uppercase letters: {uppcount}")
    print(f"Number of lowercase letters: {lowcount}")

