import random

while True:
    print("Number Guess Game")
    secret_no = random.randint(1, 20)
    chance = 5

    won = False

    for i in range(1, chance + 1):
        user = int(input(f"Attempt {i}/{chance}: Enter Guess No! "))

        if user == secret_no:
            print("🎉 You Won! Hurray!")
            won = True

            with open("History.txt", "a") as f:
                f.write(f"Won in {i} attempts\n")

            try:
                with open("BestScore.txt", "r") as f:
                    data = f.read().strip()
                    best_score = int(data) if data else None
            except FileNotFoundError:
                best_score = None

            if best_score is None or i < best_score:
                print("Top Score")
                with open("BestScore.txt", "w") as f:
                    f.write(str(i))
            else:
                print("Good Score")

            break

        elif user > secret_no:
            print("Too big, try a smaller number")
        else:
            print("Too small, try a bigger number")

    if not won:
        print("Oh! No chance over")

    replay = input("Want to play again (y/n): ").lower().strip()
    if replay != "y":
        print("Sayounara!!")
        break
