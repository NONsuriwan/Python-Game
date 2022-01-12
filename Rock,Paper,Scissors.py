import random

ผู้เล่นชนะ = 0
บอทชนะ = 0
เสมอ=0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("บอทเลือก", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("คุณชนะ!")
        ผู้เล่นชนะ += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("คุณชนะ!")
        ผู้เล่นชนะ += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("คุณชนะ!")
        ผู้เล่นชนะ += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("เสมอ!")
        เสมอ += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("เสมอ!")
        เสมอ += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("เสมอ!")
        เสมอ += 1

    else:
        print("คุณแพ้!")
        บอทชนะ += 1

print("คุณชนะ", ผู้เล่นชนะ, "ครั้ง")
print("บอทชนะ", บอทชนะ, "ครั้ง")
print("เสมอ", เสมอ, "ครั้ง")
print("ไว้มาเล่นกันอีกนะ!")
