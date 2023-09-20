# Language: Python 3
# Madison Weicht, Nishant Agarwal
# 9 September 2023
# CS 4500 Intro to Software Profession

# This program simulates two people walking on a 2D nxn board. 
# The user enters a dimension for n and a max number of moves allowed.
# The program will then simulate each person making a random move until they meet or the max moves is exceeded.

# Each person is represented as a 1x2 array which holds their position on the board as an x and y coordinate, in that order.


import numpy as np
import random as rd


# FUNCTIONS #

# Function to generate a random number in the range of 1 through 4 and returns it
def getRandom():
    randNum = rd.randrange(1, 5)
    return randNum
 
    

# Function to move a person by changing their coordinates
def movePerson(personCoords, maxCoord):

# direction calls to get a random number 1 - 4 and stores it
    direction = getRandom()

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
        if(userInteger < minValue):
            print("Please enter a value greater than", minValue)
            return False
        
        # check if over max range
        if(userInteger > maxValue):
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
    while(not inputValidator(userValue, maxValue, minValue)):
        print("Enter an integer from", minValue, "-", maxValue)
        userValue = input()

    return userValue





# MAIN FUNCTION #

# Start statement:
print("This program is a game!")
print("There are two people lost in the woods, imagine they are on a grid coordinate system.")
print("You will be inputting the dimension of the grid (a number between 0 and 100) so it is a 0 x dimension grid,")
print("and you will be inputting the maximum number of times they can move (between 0 and 1,000,000).")
print("The program will track their movements as they move in cardinal directions and then tell us if they meet within the maximum moves given!")
print("Let's begin!\n\n")



# Get dimension input from user:
print("Enter a dimension value as an integer from 0-100")
dimension = int(getNumber(99, 0))
print("You entered dimension value", dimension)


# Get maximum moves input from user:
print("\nEnter a maxMoves value as an integer from 0-1000000")
maxMoves = int(getNumber(1000000, 0))
print("You entered maxMoves value", maxMoves,"\n\n")
    
    
# Set two people variables. personA will start at 0,0, and personB will start at the opposite corner:
personA = np.array([0, 0])
personB = np.array([dimension, dimension])


# Set variables for while loop. First move will be 1, didMeet starts at false: 
currentMove = 1
didMeet = False


# while loop conditions: currentMove is less/equal to max moves and they haven't met:
while currentMove <= maxMoves and didMeet is False:
    
    # if the move is odd, personA moves, if move is even personB moves: 
    if currentMove%2 == 1:
        currentPerson = personA
    else:
        currentPerson = personB

    # move current person, calls with person and dimension value to know what the maxValue will be
    movePerson(currentPerson, dimension)
    
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



