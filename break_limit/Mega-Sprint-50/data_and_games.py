import random

def pattern():
    a="*"
    print("Strat Pattern")
    for i in range(6):
        print(a*i)

def num_game():
    secert_num=random.randint(1,20)
    print(f"{"-"*30}\n Welcome TO Number Guessing Game\n{"-"*30}")
    chance=5
    for i in range(1,chance+1):
        guess_no=int(input(f"Attemp {i}/{chance} : Enter Guessing Number : "))
        if guess_no==secert_num:
            print(f"You Won !! Subarashi \nYour Secret No is:{secert_num}\n{"-"*30}")
            break;
        elif guess_no>secert_num:
            print(f"To Big !  give a small numbar..")
        elif guess_no<secert_num:
            print(f"To Small !  give a big numbar..")
    else:
        print("Game Over ! Chance Ends Try Next Time..") 

def Student():
    name=input("Enter your name: ")
    sub=input("Enter your subject:")
    mark=int(input("Enter your total marks(1,100): "))

    dict={
            "Name":name,
            "Subject":sub,
            "Marks":mark
        }
    with open("student_data.txt","a") as f:
        f.write(str(dict))
    with open("student_data.txt","r") as f:
        print(f.read())
        
pattern()
while True:
    user=input("Did you want to play number guessing game(y/n) !")
    if user.lower=="y":
        num_game()
    else:
        print("Good By Please Try Must Be Next Time ...")
        break;
Student()         
    

