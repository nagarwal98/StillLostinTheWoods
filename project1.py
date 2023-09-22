# Language: Python 3
# Dakota Stephens, Nishant Agarwal
# 22 September 2023
# CS 4500 Intro to Software Profession

# This program simulates two people walking on a 2D nxn board.
# The user enters a dimension for n and a max number of moves allowed.
# The program will then simulate each person making a random move until they meet or the max moves is exceeded.

# Each person is represented as a 1x2 array which holds their position on the board as an x and y coordinate, in that order.


import numpy as np
import random as rd
import csv as csv


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
    # direction calls to get a random number 1 - 8 and stores it
    direction = getRandom8()

    # checks direction and moves person correspondingly:
    # direction 1 is North: if person's current y-coord is not max value, will +1
    if direction == 1:
        if personCoords[1] != maxCoord:
            personCoords[1] = personCoords[1] + 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 2 is Northeast: if person's current x-coord and y-coord is not max value, will +1 to both
    elif direction == 2:
        if personCoords[0] != maxCoord and personCoords[1] != maxCoord:
            personCoords[0] = personCoords[0] + 1
            personCoords[1] = personCoords[1] + 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 3 is East: if person's current x-coord is not max value, will +1
    elif direction == 3:
        if personCoords[0] != maxCoord:
            personCoords[0] = personCoords[0] + 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 4 is Southeast: if person's current x-coord is not max value and y-coord is not min value, will +1 x-coord and -1 y-coord
    elif direction == 4:
        if personCoords[0] != maxCoord and personCoords[1] != 0:
            personCoords[0] = personCoords[0] + 1
            personCoords[1] = personCoords[1] - 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 5 is South: if person's current y-coord is not min value (0), will -1
    elif direction == 5:
        if personCoords[1] != 0:
            personCoords[1] = personCoords[1] - 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 6 is Southwest: if person's current y-coord is not min value (0) and the persons x-coord is not min value (0), will -1 from both
    elif direction == 6:
        if personCoords[1] != 0 and personCoords[0] != 0:
            personCoords[0] = personCoords[0] - 1
            personCoords[1] = personCoords[1] - 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 7 is West: if person's current x-coord is not min value (0), will -1
    elif direction == 7:
        if personCoords[0] != 0:
            personCoords[0] = personCoords[0] - 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

    # direction 8 is Northwest: if person's current x-coord is not min value (0) and the persons y-coord is not max value, will -1 x-coord and +1 y-coord
    elif direction == 8:
        if personCoords[0] != 0 and personCoords[1] != maxCoord:
            personCoords[0] = personCoords[0] - 1
            personCoords[1] = personCoords[1] + 1
        else: # move fail, try again:
            movePersonP8(personCoords, maxCoord)

# Function to check if people have met: checks by comparing coords to see if they are equal.
def checkMeet(personA, personB):
    if np.array_equiv(personA, personB):
        return True
    else:
        return False

# prints person's postion
#def checkPosition(person):
#    print(person)

# InputValidator function checks whether an integer is in some range
def inputValidator(userInt, maxValue, minValue):
    # check if under min range
    if (userInt < minValue):
        print("Please enter a value greater than", minValue)
        return False

    # check if over max range
    if (userInt > maxValue):
        print("Please enter a value less than", maxValue)
        return False

    return True;

# checks whether an array contains all integers or not
def validateInts(checkIntArray):
    for x in checkIntArray:
        try:
            currentInt = int(x)
        except ValueError:
            return False
    return True

# function to validate a given line of input is ascending integers
def validateAscending(intArray):
    
    # check if values are integers
    if(not validateInts(intArray)):
        print("line does not contain only integer values")
        return False

    # enumerate through the array
    for index, x in enumerate(intArray):

        # break out early to avoid index out of bounds
        if(index == 4):
            return True

        # checking if the integers are ascending
        if(int(x) > int(intArray[index + 1])):
            print(" line of integers is not ascending")
            return False

    return True

# function to validate the indata.txt file
def validateFile(fileIn):
    lines = len(fileIn.readlines())
    if(lines != 6):
        print("Input file must have 6 lines")
        return False
    fileIn.seek(0)
    # first line is 5 ascending integers of dimension
    firstStr = fileIn.readline()
    firstArr = firstStr.split(',')

    if(not validateAscending(firstArr)):
        print("Line 1".rstrip())
        return False
    if(len(firstArr) != 5):
        print("Line 1 requires 5 ascending integers")
        return False
    for x in firstArr:
        if(not inputValidator(int(x), 99, 0)):
            print("Line 1 dimension values must be in range 0-100")
            return False

    # second line is 3 integers P, M, R
    secondStr = fileIn.readline()
    secondArr = secondStr.split(',')

    if(not validateInts(secondArr)):
        print("Line 2".rstrip())
        return False
    if(len(secondArr) != 3):
        print("Line 2 requires 3 integers")
        return False
    if(int(secondArr[0]) != 4 and int(secondArr[0] != 8)):
        print("Line 2 protocol number must be 4 or 8")
        return False
    if(not inputValidator(int(secondArr[1]), 1000000, 1)):
        print("Line 2 max moves must be in range 1-1000000")
        return False
    if(not inputValidator(int(secondArr[2]), 100000, 1)):
        print("Line 2 repetition values must be in range 1-100000")
        return False


    # third line is 5 ascending integers of repetitions
    thirdStr = fileIn.readline()
    thirdArr = thirdStr.split(',')

    if(not validateAscending(thirdArr)):
        print("Line 3".rstrip())
        return False
    if(len(thirdArr) != 5):
        print("Third line requires 5 ascending integers")
        return False
    for x in thirdArr:
        if(not inputValidator(int(x), 100000, 1)):
            print("Third line repetition values must be in range 1-100000")
            return False

    # fourth line is 3 integers D, P, M
    fourthStr = fileIn.readline()
    fourthArr = fourthStr.split(',')

    if(not validateInts(fourthArr)):
        print("Line 4".rstrip())
        return False
    if(len(fourthArr) != 3):
        print("Fourth line of input requires 3 integers")
        return False
    if(not inputValidator(int(fourthArr[0]), 99, 0)):
        print("Line 4 dimension values must be in range 0-99")
        return False
    if(int(fourthArr[1]) != 4 and int(fourthArr[1] != 8)):
        print("Line 4 protocol number must be 4 or 8")
        return False
    if(not inputValidator(int(fourthArr[2]), 1000000, 1)):
        print("Line 4 max moves must be in range 1-1000000")
        return False

    # fifth line is protocols 4,4,8,8
    fifthStr = fileIn.readline()

    if(fifthStr.rstrip() != '4,4,8,8'):
        print("Fifth line of input must be '4,4,8,8'")
        return False

    # sixth line is 3 intgers D, M, R
    sixthStr = fileIn.readline()
    sixthArr = sixthStr.split(',')

    if(not validateInts(sixthArr)):
            print("Line 6".rstrip())
            return False
    if(len(sixthArr) != 3):
        print("Sixth line of input requires 3 integers")
        return False
    if(not inputValidator(int(sixthArr[0]), 99, 0)):
        print("Line 6 dimension values must be in range 0-99")
        return False
    if(not inputValidator(int(sixthArr[1]), 1000000, 1)):
        print("Line 6 max moves must be in range 1-1000000")
        return False
    if(not inputValidator(int(sixthArr[2]), 100000, 1)):
        print("Line 6 repetition values must be in range 1-100000")
        return False

    return True

def runSingleExperimentRepitition(dimension, protocol, moves):


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
    ''' Replaced the following block due to commented out code.
    if didMeet:
        # print the move that they met on:
        # print("The two did meet on move", currentMove)

        # print Position they met at:
        # print("They met at postion:")
        # checkPosition(personA)

    else:
        # print("Unfortunately, the two did not meet! Despite moving", maxMoves, "times!")
        currentMove = maxMoves
        # This is needed because current moves is one larger than maxMoves when we run out of moves.
    '''
    # replaced above block with this if check:
    if not didMeet:
        currentMove = maxMoves
    return currentMove

def calcAvg(listOfValues):
    totalValue = 0
    for value in listOfValues:
        totalValue += value
    avg = totalValue / len(listOfValues)
    return avg


# run R simulated wanderings in a grid of size D X D. Use protocol P for each move M
def runExperiments(dimension, protocol, moves, numberSimulations):
    # print(f"\n******Running Experiment with dimension: {dimension}, protocol: {protocol}, and Max Moves: {moves}******\n")
    # declare all local variables that will be returned and used.
    lowestMoves = moves
    highestMoves = 0
    # averageMovesItems = []
    sumMoves = 0
    averageMoves = 0
    # this works because range() does not include the final number in the specified range.
    for n in range(numberSimulations):
        # print(f"\nRunning Simulation {n+1} of {numberSimulations}")
        # This function outputs lowest number of moves, highest number of moves, and average number of moves.
        madeMoves = runSingleExperimentRepitition(dimension, protocol, moves)
        if(madeMoves < lowestMoves): lowestMoves = madeMoves
        if(madeMoves > highestMoves): highestMoves = madeMoves
        # averageMovesItems.append(madeMoves)
        sumMoves += madeMoves
        # print(f"End of Simulation {n+1} of {numberSimulations}\n")
    # count up the moves made and get the average:
    
    averageMoves = sumMoves / numberSimulations # old way: calcAvg(averageMovesItems)
    # print(f"EXPERIMENT INFO: Low: {lowestMoves}, High: {highestMoves}, and Average: {averageMoves}")
    # print("\n******END OF EXPERIMENT******\n")
    return lowestMoves, highestMoves, averageMoves


# MAIN FUNCTION #

# Start statement:
print("This program is a game!")
print("There are two people lost in the woods, imagine they are on a grid coordinate system.")
print("You will be inputting the dimension of the grid (a number between 0 and 99) so it is a 0 x dimension grid,")
print("and you will be inputting the maximum number of times they can move (between 0 and 1,000,000).")
print(
    "The program will track their movements as they move in cardinal directions and then tell us if they meet within the maximum moves given!")
print("Let's begin!\n\n")


# opening file and validating input data
fileIn = open("indata.txt", "r")
fileOut = open("outdata.txt", "w")

if(not validateFile(fileIn)):
    print("Invalid input file format. Please try again.")
else:
    fileIn.seek(0)

    ### EXPERIMENT 1 ###

    firstStr = fileIn.readline()
    firstArr = firstStr.split(',')
    secondStr = fileIn.readline()
    secondArr = secondStr.split(',')

    protocol = int(secondArr[0])
    maxMoves = int(secondArr[1])
    repetitions = int(secondArr[2])

    print('Experiment 1 changes the dimensions of the grid. Other variables are held constant.')
    fileOut.write('Experiment 1 changes the dimensions of the grid. Other variables are held constant.\n')
    print('-------------------------------------------------------------------------------------')
    fileOut.write('-------------------------------------------------------------------------------------\n')
    print('|           | Maximum   | Number of |           | Lowest    | Highest   | Average   |')
    fileOut.write('|           | Maximum   | Number of |           | Lowest    | Highest   | Average   |\n')
    print('| DIMENSIONS| Moves     | Repeats   | Protocol  | Moves     | Moves     | Moves     |')
    fileOut.write('| DIMENSIONS| Moves     | Repeats   | Protocol  | Moves     | Moves     | Moves     |\n')
    print('-------------------------------------------------------------------------------------')
    fileOut.write('-------------------------------------------------------------------------------------\n')
    for dimensionStr in firstArr:
        dimension = int(dimensionStr)
        low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
        print('| %10d| %10d| %10d| %10d| %10d| %10d| %10f|' % (dimension, maxMoves, repetitions, protocol, low, high, avg))
        fileOut.write('| %10d| %10d| %10d| %10d| %10d| %10d| %10f|\n' % (dimension, maxMoves, repetitions, protocol, low, high, avg))

    print('-------------------------------------------------------------------------------------')
    fileOut.write('-------------------------------------------------------------------------------------\n')

     ### EXPERIMENT 2 ###

    thirdStr = fileIn.readline()
    thirdArr = thirdStr.split(',')
    fourthStr = fileIn.readline()
    fourthArr = fourthStr.split(',')

    dimension = int(fourthArr[0])
    protocol = int(fourthArr[1])
    maxMoves = int(fourthArr[2])
    
    print('Experiment 2 changes the number of wanderings (repeats) for each row. Other variables are held constant.')
    fileOut.write('Experiment 2 changes the number of wanderings (repeats) for each row. Other variables are held constant.\n')
    print('--------------------------------------------------------------------------------------')
    fileOut.write('--------------------------------------------------------------------------------------\n')
    print('| NUMBER OF |            | Maximum   |           | Lowest    | Highest   | Average   |')
    fileOut.write('| NUMBER OF |            | Maximum   |           | Lowest    | Highest   | Average   |\n')
    print('| REPEATS   | Dimensions | Moves     | Protocol  | Moves     | Moves     | Moves     |')
    fileOut.write('| REPEATS   | Dimensions | Moves     | Protocol  | Moves     | Moves     | Moves     |\n')
    print('--------------------------------------------------------------------------------------')
    fileOut.write('--------------------------------------------------------------------------------------\n')

    for repetitionStr in thirdArr:
        repetitions = int(repetitionStr)
        low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
        print('| %10d| %11d| %10d| %10d| %10d| %10d| %10f|' % (repetitions, dimension, maxMoves, protocol, low, high, avg))
        fileOut.write('| %10d| %11d| %10d| %10d| %10d| %10d| %10f|\n' % (repetitions, dimension, maxMoves, protocol, low, high, avg))
        
    print('--------------------------------------------------------------------------------------')
    fileOut.write('--------------------------------------------------------------------------------------\n')

    ### EXPERIMENT 3 ###

    fifthStr = fileIn.readline()
    fifthArr = fifthStr.split(',')
    sixthStr = fileIn.readline()
    sixthArr = sixthStr.split(',')

    dimension = int(sixthArr[0])
    maxMoves = int(sixthArr[1])
    repetitions = int(sixthArr[2])

    for protocolStr in fifthArr:
        protocol = int(protocolStr)
       # low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
       # print(f"EXPERIMENT 3: Low: {low}, High: {high}, and Average: {avg}")




    #dimension = int(getNumber(99, 0))
    #maxMoves = int(getNumber(1000000, 0))

    # Note the input for function run runExperiements:
    # runExperiements(Dimension (0 - 99), Protocol (8 or 4), Max player moves (0 - 1Mil), Number of Simulations (# of times to repeat with the three earlier values))
    # Note, this function gives an output of low, high, and average.

    #low, high, avg = runExperiments(dimension, 4, maxMoves, 3)
    #print(f"EXPERIMENT 1: Low: {low}, High: {high}, and Average: {avg}")
    #low, high, avg = runExperiments(dimension, 8, maxMoves, 1)
    #print(f"EXPERIMENT 2: Low: {low}, High: {high}, and Average: {avg}")
    #low, high, avg = runExperiments(dimension, 4, maxMoves, 4)
    #print(f"EXPERIMENT 3: Low: {low}, High: {high}, and Average: {avg}")
    #low, high, avg = runExperiments(dimension, 8, maxMoves, 5)
    #print(f"EXPERIMENT 4: Low: {low}, High: {high}, and Average: {avg}")


    print("Good-bye! Thank you for playing! <(￣︶￣)>")
