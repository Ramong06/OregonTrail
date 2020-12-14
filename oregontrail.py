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

#Choosing Difficulty Setting
print("Choose your difficulty level")
difficultyLevel = input('(Easy, Normal, Hard, El Rancho Style)')
while len(difficultyLevel) >= 0:
    #Easy Mode
    if difficultyLevel == "Easy":
        foodNum = 1000
        healthNum = 10
        break
    #Normal Mode
    if difficultyLevel == "Normal":
        foodNum = 500
        healthNum = 7
        break
    #Hard Mode
    if difficultyLevel == "Hard":
        foodNum = 300
        healthNum = 4
        break
    #El Rancho Style Mode
    if difficultyLevel == "El Rancho Style":
        foodNum = 100
        healthNum = 3
        break
    else:
        print("You must choose a difficulty level, check your spelling.")
        difficultyLevel = input('(Easy, Normal, Hard, El Rancho Style)')

#Value settings
distanceMoved = 0
monthNum = 3
daysPass = 1
totalDays = 0
monthsWithThirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
randomResult = 0
healthD1 = random.randint(1, 31)
healthD2 = random.randint(1, 31)
accidentAppearance = random.randint(1, 30)
travelDistance = 0
restTime = 0
huntTime = 0
statusNum = 0
monthAppear = "March"

#Days
def addDays(min, max):
    global daysPass
    global monthNum
    global monthsWithThirtyOneDays
    global randomResult
    global foodNum
    global healthNum
    global healthD1
    global healthD2
    global totalDays
    global accidentAppearance

    randomResult = random.randint(min, max)
    print("Now", randomResult, "days passed.")
    days_pass_min = daysPass
    check_big = daysPass + randomResult

    #Accident
    if accidentAppearance >= daysPass and accidentAppearance <= check_big
        a_number = random.randint(1, 3)
        a_health_num = random.randint(1, 2)
        if a_number == 1:
            print("You just crossed a Sendero")
            if a_number == 2:
                print("You have contracted Ojo")
            if a_number == 3:
                print("You have went to a baile and had a good time.")
                random_result2_food = random.randint(1, 10)
                random_result2_day = random.randint(1, 10)
                print("You eat " + str(random_result2_food) + " lbs extra food.")
                print("It also took up extra")




