# Here is my first python project; a PC game/quiz that keeps track of your answers!

print("Welcome to my PC game!")

# input is where my program's user can type something into a prompt.

playing = input("Do you want to play? ")

# Set conditions for my user's 'playing' response via conditional statement:
# "if user answer is anything but 'yes' (!=), quit program".
# adding '.lower()' automatically turns whatever my user types into lower-case.
# My specified correct answer must be lower-case, so that's why '.lower()' is useful here.

if playing.lower() != "yes":
        quit()

# "if user entered Yes, YES, or any variation of yEs, print this and also begin keep score."

print("Okay! Then let's play :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("You're absolutely correct!")
    score += 1
     
else:
    print("That's incorrect. Please try again.")

# Incorrect User answers = 0 points and continues.
# Correct User answers = +1 point and continues.

answer = input("Now how about this; How many threads exist on a single PC's core? ")

if answer == "2":
    print("Right again!")
    score += 1
else:
    print("That's incorrect. Please try again.")

answer = input("Hmmmmm... Let me think... What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Nice one!")
    score += 1
else:
    print("That's incorrect. Please try again.")

answer = input("Okay, but are you aware of what GPU stands for? ")

if answer.lower() == "graphics processing unit":
    print("You're too good at this!")
    score += 1
else:
    print("That's incorrect. Please try again.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " % correct!")
