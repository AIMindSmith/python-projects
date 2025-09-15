import random 

user_wins =0
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        quit()

    if user_input not in options:
        print("please type a valid option")
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("computer picked", computer_pick + " you picked " + user_input)

    if user_input == "rock" and computer_pick == "scissor":
        print("you win")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("you win")
        user_wins += 1
    else:
        print("you lose")
        computer_wins += 1

    print("you won", user_wins, "times")
    print("computer won", computer_wins, "times")
    print("goodbye")
