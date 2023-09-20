# Language: Python 3
# Dakota Stephens, Nishant Agarwal
# 20 September 2023
# CS 4500 Intro to Software Profession

# This program simulates two people walking on a 2D nxn board.
# The user enters a dimension for n and a max number of moves allowed.
# The program will then simulate each person making a random move until they meet or the max moves is exceeded.

# Each person is represented as a 1x2 array which holds their position on the board as an x and y coordinate, in that order.


import numpy as np
import random as rd


# FUNCTIONS #

# Function to generate a random number in the range of 1 through 5 (not included) and returns it
def getRandom4():
    randNum = rd.randrange(1, 5)
    return randNum


# returns a number between 1 (included) and 9 (not included)
def getRandom8():
    randNum = rd.randrange(1, 9)
    return randNum


# decides protocol to be used:
def protocolChoice(pValue, personCoords, maxCoord):
    if pValue == 4:
        movePersonP4(personCoords, maxCoord)
    elif pValue == 8:
        movePersonP8(personCoords, maxCoord)
    else:
        print(f"Failed to make protocol choice given input of {pValue}")


# Function to move a person by changing their coordinates
def movePersonP4(personCoords, maxCoord):
    # direction calls to get a random number 1 - 4 and stores it
    direction = getRandom4()

    # checks direction and moves person correspondingly:
    # direction 1 is North: if person's current y-coord is not max value, will +1
    if direction == 1:
        if personCoords[1] != maxCoord:
            personCoords[1] = personCoords[1] + 1

    # direction 2 is East: if person's current x-coord is not max value, will +1
    elif direction == 2:
        if personCoords[0] != maxCoord:
            personCoords[0] = personCoords[0] + 1

    # direction 3 is South: if person's current y-coord is not min value (0), will -1
    elif direction == 3:
        if personCoords[1] != 0:
            personCoords[1] = personCoords[1] - 1

    # direction 4 is West: if person's current x-coord is not min value (0), will -1
    elif direction == 4:
        if personCoords[0] != 0:
            personCoords[0] = personCoords[0] - 1


# Function to move a person by changing their coordinates (However, this needs to handle diagonal moves)
def movePersonP8(personCoords, maxCoord):
    # direction calls to get a random number 1 - 4 and stores it
    direction = getRandom8()

    ''' Need to modify the code below to support 8 directions:'''

    # checks direction and moves person correspondingly:
    # direction 1 is North: if person's current y-coord is not max value, will +1
    if direction == 1:
        if personCoords[1] != maxCoord:
            personCoords[1] = personCoords[1] + 1

    # direction 2 is East: if person's current x-coord is not max value, will +1
    elif direction == 2:
        if personCoords[0] != maxCoord:
            personCoords[0] = personCoords[0] + 1

    # direction 3 is South: if person's current y-coord is not min value (0), will -1
    elif direction == 3:
        if personCoords[1] != 0:
            personCoords[1] = personCoords[1] - 1

    # direction 4 is West: if person's current x-coord is not min value (0), will -1
    elif direction == 4:
        if personCoords[0] != 0:
            personCoords[0] = personCoords[0] - 1


# Function to check if people have met: checks by comparing coords to see if they are equal.
def checkMeet(personA, personB):
    if np.array_equiv(personA, personB):
        return True
    else:
        return False


# prints person's postion
def checkPosition(person):
    print(person)


# InputValidator function checks whether a user value is an integer in some range
def inputValidator(userIn, maxValue, minValue):
    # check whether user input is an integer
    try:
        userInteger = int(userIn)

        # check if under min range
        if (userInteger < minValue):
            print("Please enter a value greater than", minValue)
            return False

        # check if over max range
        if (userInteger > maxValue):
            print("Please enter a value less than", maxValue)
            return False

        return True;

    except ValueError:
        print("Please enter a valid integer")
        return False


# getNumber function retrieves a value between a range and calls inputValidator
def getNumber(maxValue, minValue):
    userValue = input()

    # reprompt on bad input
    while (not inputValidator(userValue, maxValue, minValue)):
        print("Enter an integer from", minValue, "-", maxValue)
        userValue = input()

    return userValue


def runSingleExperiment(dimension, protocol, moves):
    print(
        f"\n******Running Experiment with dimension: {dimension}, protocol: {protocol}, and Max Moves: {moves}******\n")

    # Get maximum moves from input
    maxMoves = moves

    # Set two people variables. personA will start at 0,0, and personB will start at the opposite corner:
    personA = np.array([0, 0])
    personB = np.array([dimension, dimension])

    # Set variables for while loop. First move will be 1, didMeet starts at false:
    currentMove = 1
    didMeet = False

    # while loop conditions: currentMove is less/equal to max moves and they haven't met:
    while currentMove <= maxMoves and didMeet is False:

        # if the move is odd, personA moves, if move is even personB moves:
        if currentMove % 2 == 1:
            currentPerson = personA
        else:
            currentPerson = personB

        # move current person, calls with person and dimension value to know what the maxValue will be
        protocolChoice(protocol, currentPerson, dimension)

        # check if people have met:
        didMeet = checkMeet(personA, personB)

        # add 1 to currentMove to progress:
        currentMove += 1

    # After loop, if they met:
    if didMeet:
        # print the move that they met on:
        print("The two did meet on move", currentMove)

        # print Position they met at:
        print("They met at postion:")
        checkPosition(personA)
        print('\n')

    else:
        print("Unfortunately, the two did not meet! Despite moving", maxMoves, "times!\n\n")

    print("Good-bye! Thank you for playing! <(￣︶￣)>")
    print("\n******END OF EXPERIMENT******\n")


# run R simulated wanderings in a grid of size D X D. Use protocol P for each move M
def runExperiments(dimension, protocol, moves, numberSimulations):
    # this works because range() does not include the final number in the specified range.
    for n in range(numberSimulations):
        print(f"Running Simulation {n + 1} of {numberSimulations + 1}")
        runSingleExperiment(dimension, protocol, moves)


# MAIN FUNCTION #

# Start statement:
print("This program is a game!")
print("There are two people lost in the woods, imagine they are on a grid coordinate system.")
print("You will be inputting the dimension of the grid (a number between 0 and 99) so it is a 0 x dimension grid,")
print("and you will be inputting the maximum number of times they can move (between 0 and 1,000,000).")
print(
    "The program will track their movements as they move in cardinal directions and then tell us if they meet within the maximum moves given!")
print("Let's begin!\n\n")


#### Need to input file read here. ####


# Get dimension input from user:
print("Enter a dimension value as an integer from 0-99")
dimension = int(getNumber(99, 0))
print("You entered dimension value", dimension)

# Get maximum moves input from user:
print("\nEnter a maxMoves value as an integer from 0-1000000")
maxMoves = int(getNumber(1000000, 0))
print("You entered maxMoves value", maxMoves, "\n\n")

# Note the input for function run runExperiements:
#runExperiements(Dimension (0 - 99), Protocol (8 or 4), Max player moves (0 - 1Mil), Number of Simulations (# of times to repeat with the three earlier values))
runExperiments(dimension, 4, maxMoves, 3) 
runExperiments(dimension, 8, maxMoves, 1)
runExperiments(dimension, 4, maxMoves, 4)
runExperiments(dimension, 8, maxMoves, 5)

