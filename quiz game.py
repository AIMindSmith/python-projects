print("hello")
print("welcome to quiz game")
print("what is your name :")
name=input().capitalize()
print("hello",name)

playing = input("do you want to play quiz game ? ").lower()
if playing != "yes":
    quit()



print("ok lets play :)")
score = 0

print("first question")
answer = input("what dose cpu stan for ?").lower()
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
    print("correct answer is central processing unit")
    quit()


print("second question")
answer = input("what dose ram stan for ?").lower()
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print('incorrect')
    print("correct answer is random access memory")
    quit()


print("thir question")
answer = input("what dose gpu stan for ?").lower()
if answer == "graphics processing unit":
    print("correct")    
    score += 1
else:

    print("incorrect")
    print("correct answer is graphics processing unit")
    quit()


print("fourth question")
answer = input("what dose usb stan for ?").lower()
if answer == "universal serial bus":
    print("correct")
    score += 1
else:
    print("incorrect")
    print("correct answer is universal serial bus")
    quit()


print("you got " + str(score) + " questions correct")
print("you got " + str((score / 4) * 100) + "%")