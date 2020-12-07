import random
import time

#welcome player to game
print("Welcome to the Oregon Trail")

#Ask for Name
playerName = input("What's your name?")
while len(playerName) >= 0:
    if len(playerName) > 0:
        print(str(playerName) + " is a great name!")
        break


