#snake water gun game

import random
choice = random.randint(1,3)
num_to_choice = {
    1:"rock",
    2:"paper",
    3:"scissor"
}
print("Choose between 1-3\nRock:1\nPaper:2\nScissor:3")
user_input = int(input("Enter you choice: "))
computer = num_to_choice.get(choice)
print(f"Computer chose: {computer}")
user = num_to_choice.get(user_input)
print(f"You chose: {user}")
if user == "rock" and computer == "rock":
    print("Draw")
elif user == "rock" and computer == "paper":
    print("Computer Won!")
elif user == "rock" and computer == "scissor":
    print("You Won!")
elif user == "paper" and computer == "rock":
    print("You Won!")
elif user == "paper" and computer == "paper":
    print("Draw")
elif user == "paper" and computer == "scissor":
    print("Computer Won!")
elif user == "scissor" and computer == "rock":
    print("Computer Won!")
elif user == "scissor" and computer == "paper":
    print("You Won!")
elif user == "scissor" and computer == "scissor":
    print("Draw")
else:
    print("Choose between 1-3\nRock:1\nPaper:2\nScissor:3")


