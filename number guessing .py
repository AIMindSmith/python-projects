import random
print("welcome to number guessing game")
print("what is your name :")
name = input().capitalize()
playing = input("do you want to play number guessing game ? ").lower()
if playing == "yes":
    print("lets start the game")
    

# print("guess a number between 1 to 10")
# number = random.randint(1, 11)
# guess = int(input("enter your guess : "))
# if guess == number:
#     print("you guessed right")
# else:
#     print("you guessed wrong")

#     print("the number is", number)
#     quit()


top_of_range = input("type a number : ")


top_of_range.isdigit()
top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("please type a number greater than 0 next time")
    quit()
else:
    print("lets start the game")

    random_number = random.randint(0, top_of_range)
    print(random_number)

while True:
    guesses += 1
    guess = input("make a guess : ")
    guess.isdigit()
    guess = int(guess)

    if guess < 0:
        print("please type a number greater than 0 next time")
        continue

    if guess == random_number:
        print("you guessed right")
        break
    else:
        print("you guessed wrong")
        print("the number is", random_number)
    print("you took", guesses, "guesses")

