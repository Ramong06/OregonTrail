import random
import time

#welcome player to game
print("Welcome to the South Texas Trail!")

#Ask for Name
playerName = input("What's your name?")
while len(playerName) >= 0:
    if len(playerName) > 1:
        print(str(playerName) + " is a great name!")
        break
    if len(playerName) == 1:
        playerNameChoice = input(str(playerName) + "? Is your name really only 1 letter? (y/n):")
        if playerNameChoice == "y" or playerNameChoice == "Y":
            print("Well, that's great!")
            break
        if playerNameChoice == "n" or playerNameChoice == "N":
            playerName = input("Well, what is your name?")
        else:
            print("You didn't type anything, try again :) ")
            playerName = input("What is your name?")

print("Choose your difficulty level")
difficultyLevel = input('(Easy, Normal, Hard, El Rancho Style)')





