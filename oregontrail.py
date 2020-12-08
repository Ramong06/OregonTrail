import random
import time

#welcome player to game
print("Welcome to the Oregon Trail")

#Ask for Name
playerName = input("What's your name?")
while len(playerName) >= 0:
    if len(playerName) > 1:
        print(str(playerName) + " is a great name!")
        break
    if len(playerName) == 1:
        playerNameChoice = input(str(playerName) + "? Is your name really only 1 letter?(y/n):")
        if playerNameChoice == "y" or playerNameChoice == "Y":
            print("Well, that's great, too!...")
            break



