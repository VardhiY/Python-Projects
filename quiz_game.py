print("Welcome to my computer quiz!")

playing=input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score=0
answer=input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer=input("What does GPU stand for?").lower()
if answer == "graphics processing unit":
    print('correct!')
    score += 1
    else:
    print("Incorrect!")
    

answer=input("What does RAM stand for?").lower()
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer=input("What does ROM stand for?").lower()
if answer == "read only memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score /4)*100)+"%.")