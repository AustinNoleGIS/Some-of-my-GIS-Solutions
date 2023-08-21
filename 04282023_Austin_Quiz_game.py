# Here is my first python project; a PC game/quiz that keeps track of your answers!

print("Welcome to my PC game!")

# input is where my program's user can type something into a prompt.
playing = input("Do you want to play? ")

# Set conditions for my user's 'playing' response via conditional statement:
# "if user answer is anything but 'yes' (!=), quit program".
# adding '.lower()' automatically turns whatever my user types into lower-case.
if playing.lower() != "yes":
        quit()

# "if user entered Yes, YES, or any variation of yEs, print this and also begin keep score.""
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

# S P A C E S
# what if ____?
# Boolean Logic with Operators 'or, and, not'.  how about 'yes' AND 'y'  ??
#   Conditional + Boolean logic = more complex conditional statements!

# Boolean logic = True or False. = only 1 correct condition/Output.
#         If I had TWO condtions, I STILL need my 1 correct output.
#   'Truth Table' in programming
#    input 1, input 2, True, False,   OR,  AND,  sometimes NOT or NOR or XOR.
#    AND = show me the overlap of Cond. A and Cond. B.
#    OR  = show me Cond. A or Cond. B.
#   Logic is ALWAYS True or False.

#   =  ==   !=   &&   ||    just like SQL syntax! Boolean Logic is good to know!!  "Discrete Math"

#loop back to start of Entire program AT THE END
#loop back for individual incorrectly andwered questions.