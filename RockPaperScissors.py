import random
import os
import time


choices = ["1", "2", "3"]
wins = 0
loses = 0
ties =0


while True:
    os.system('clear')
    print("WINS:",wins)
    print("LOSES:",loses)
    print("TIES:",ties)

    print("\n1: Rock")
    print("2: Paper")
    print("3: Scissors")
    print("0: ESCAPE\n")


    userChoice = str(input("Your choice: "))
    if userChoice == "0":
        quit()
    #If choice is invalid
    while userChoice not in choices:
        userChoice = str(input("Something went wrong. Chose again: "))

    compChoice = str(random.randrange(0, 100)%3+1)
    

    if userChoice == compChoice:
        print("\nTIE")
        ties+=1
    elif (userChoice == "1" and compChoice == "3") or (userChoice == "3" and compChoice == "1") or (userChoice == "2" and compChoice == "1"):
        print("\nYOU WON :)")
        wins+=1
    else:
        print("\nYOU LOOSE :(")
        loses+=1
    
    time.sleep(0.5)