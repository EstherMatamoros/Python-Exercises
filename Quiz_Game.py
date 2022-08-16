#Quiz Game
print("Welcome to my computer quiz!")


playing = input("Do yo want to play? ") #ask the user to write something in the console with a prompt, which goes sinside the ()

if playing.lower() != "yes":
    quit() #Terminate the program

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print ("Correct!")
    score += 1 # equals to score = score + 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print ("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print ("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print ("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")