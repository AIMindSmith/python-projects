name = input("What is your name? ")
print("Hello " + name + ", welcome to the adventure game!")

answer = input("You are in a dark room. There is a door to your left and right. Which one do you take? (left/right) ").lower()
if answer =="left":
    print("You enter a room full of beasts. Game Over.")
elif answer == "right":
    print("You find a treasure chest. You open it and find gold! You Win!")
else:
    print("You choose a path that doesn't exist. Game Over.")



answer = input("You see a river. Do you want to swim across or build a raft? (swim/raft) ").lower()
if answer == "swim":
    print("You were eaten by a crocodile. Game Over.")
elif answer == "raft":
    print("You safely crossed the river and found a village. You Win!")
else:
    print("You choose a path that doesn't exist. Game Over.")
answer = input("You enter a village. There is a merchant who offers you a sword. Do you want to buy it? (yes/no) ").lower()
if answer == "yes":
    print("You bought the sword and used it to defeat the dragon. You Win!")
elif answer == "no":
    print("You were eaten by the dragon. Game Over.")
else:
    print("You choose a path that doesn't exist. Game Over.")   


    print("Thank you for playing, " + name + "!")