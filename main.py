print("Welcome to my quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')

answer = input("What does jk stand for? ")
if answer.lower() == "jai kutty":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')

answer = input("What is the first color of the rainbow? ")
if answer.lower() == "red":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")