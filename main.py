import random

user_score = 0
computer_score = 0

options = ["rock","paper","scissor"]

user_win_input = int(input("Set the winning points: "))

while True:

    user_input = input("Pick rock/paper/scissor or Q to quit and get the score: ").lower()

    if user_input == "q":
        break

    if user_input not in ["rock","paper","scissor"]:
        continue

    random_number = random.randint(0,2)
    computer_choice = options[random_number]

    print(f"Computer picked {computer_choice}")

    if user_input == "rock" and computer_choice == "scissor":
        print("You won :)")
        user_score += 1
        if user_score == user_win_input:
            print("You won the game :) Hurray")
            break
        elif computer_score == user_win_input:
            print("You lost the game :( Better luck next time!")

    elif user_input == "paper" and computer_choice == "rock":
        print("You won :)")
        user_score += 1
        if user_score == user_win_input:
            print("You won the game :) Hurray")
            break
        elif computer_score == user_win_input:
            print("You lost the game :( Better luck next time!")
    elif user_input == "scissor" and computer_choice == "paper":
        print("You won :)")
        user_score += 1
        if user_score == user_win_input:
            print("You won the game :) Hurray")
            break
        elif computer_score == user_win_input:
            print("You lost the game :( Better luck next time!")
    elif user_input == computer_choice:
        print("You and the computer picked the same thing")
    else:
        print("You lost :(")
        computer_score += 1
        if user_score == user_win_input:
            print("You won the game :) Hurray")
            break
        elif computer_score == user_win_input:
            print("You lost the game :( Better luck next time!")

print(f"Your score is {user_score} and computer's score is {computer_score}")
print("Good bye!")
