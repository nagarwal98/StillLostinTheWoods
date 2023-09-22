# Language: Python 3
# Dakota Stephens, Nishant Agarwal
# 22 September 2023
# CS 4500 Intro to Software Profession

# This program simulates two people wondering on a 2D nxn board (called a forest).
# The program will run 3 experiments varying the board dimensions, the way the people move (protocol), and repetitions per Simulation
# Input data is parsed through an indata.txt file, and output will be sent to outdata.txt
# The two people lost in the woods are taking random turns to move in order to try and find the other person.
# The people are going to be trying to find eachother given different inputs of Grid Dimension, Maximum Moves, and Movement Protocol
# These different modifications to variables between runs will be called experiments.
# Movement Protocol 4 allows for movement in the four cardinal directions but fails to move when trying to move outside the grid.
# Movement Protocol 8 is like Movement Protocol 4 but allows for diagonal movement and reattempts a new move when trying to move outside of the grid.
# We will be running 3 of these experiments based on the input data given in the file indata.txt
# The simulations, in many cases, will be repeated multiple times for better accuracy of the results.
# a simulation is one insteance of a random wondering test.

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


# InputValidator function checks whether an integer is in some range
def inputValidator(userInt, maxValue, minValue):
    # check if under min range
    if (userInt < minValue):
        return False

    # check if over max range
    if (userInt > maxValue):
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
        print("Line contains an invalid integer:")
        return False

    # enumerate through the array
    for index, x in enumerate(intArray):

        # break out early to avoid index out of bounds
        if(index == 4):
            return True
        try:
            # checking if the integers are ascending
            if(int(x) > int(intArray[index + 1])):
                print("Line of integers is not ascending:")
                return False
        except IndexError:
            print("Line does not correct number of integers:")
            return False

    return True

# function to validate the indata.txt file
def validateFile(fileIn):
    try:
    # check to see whether the file contains 6 and only 6 lines
        lines = len(fileIn.readlines())
    except:
        print("File indata.txt could not be read")
        exit()
    if(lines != 6):
        print("Input file must have 6 lines")
        return False
    fileIn.seek(0)

    # Reading in all lines and storing as arrays
    # first line is 5 ascending integers of dimension
    firstStr = fileIn.readline()
    # second line is 3 integers P, M, R
    secondStr = fileIn.readline()
    # third line is 5 ascending integers of repetitions
    thirdStr = fileIn.readline()
    # fourth line is 3 integers D, P, M
    fourthStr = fileIn.readline()
    # fifth line is protocols 4,4,8,8
    fifthStr = fileIn.readline()
    # sixth line is 3 intgers D, M, R
    sixthStr = fileIn.readline()


    # Checking for whitespace in each line
    if(' ' in firstStr):
        print("Line 1 cannot contain any whitespace")
        return False
    if(' ' in secondStr):
        print("Line 2 cannot contain any whitespace")
        return False
    if(' ' in thirdStr):
        print("Line 3 cannot contain any whitespace")
        return False
    if(' ' in fourthStr):
        print("Line 4 cannot contain any whitespace")
        return False
    if(' ' in fifthStr):
        print("Line 5 cannot contain any whitespace")
        return False
    if(' ' in sixthStr):
        print("Line 6 cannot contain any whitespace")
        return False
    if('\n' in sixthStr):
        print("Line 6 cannot contain any newline characters")
        return False

    firstArr = firstStr.strip().split(',')
    secondArr = secondStr.strip().split(',')
    thirdArr = thirdStr.strip().split(',')
    fourthArr = fourthStr.strip().split(',')
    sixthArr = sixthStr.strip().split(',')


    # Checking if each line length is correct
    if(len(firstArr) != 5):
        print("Line 1 requires 5 ascending integers")
        return False
    if(len(secondArr) != 3):
        print("Line 2 requires 3 integers")
        return False
    if(len(thirdArr) != 5):
        print("Line 3 requires 5 ascending integers")
        return False
    if(len(fourthArr) != 3):
        print("Line 4 of input requires 3 integers")
        return False
    if(len(sixthArr) != 3):
        print("Line 6 of input requires 3 integers")
        return False

    # Checking if line 5 is correct
    if(fifthStr.rstrip() != '4,4,8,8'):
        print("Line 5 of input must be '4,4,8,8'")
        return False


    # Checking if integers are in ascending order, and they are actually integers
    if(not validateAscending(firstArr)):
        print("Line 1")
        return False
    if(not validateInts(secondArr)):
        print("Line 2 requires 3 valid integers")
        return False
    if(not validateAscending(thirdArr)):
        print("Line 3")
        return False
    if(not validateInts(fourthArr)):
        print("Line 4 requires 3 valid integers")
        return False
    if(not validateInts(sixthArr)):
        print("Line 6")
        return False


    # Checking if values are in acceptable range
    # Line 1
    for x in firstArr:
        if(not inputValidator(int(x), 99, 0)):
            print("Line 1 dimension values must be in range 0-99")
            return False
    # Line 2
    if(int(secondArr[0]) != 4 and int(secondArr[0]) != 8):
        print("Line 2 protocol number must be 4 or 8")
        return False
    if(not inputValidator(int(secondArr[1]), 1000000, 1)):
        print("Line 2 max moves must be in range 1-1000000")
        return False
    if(not inputValidator(int(secondArr[2]), 100000, 1)):
        print("Line 2 repetition value must be in range 1-100000")
        return False
    # Line 3
    for x in thirdArr:
        if(not inputValidator(int(x), 100000, 1)):
            print("Line 3 repetition values must be in range 1-100000")
            return False
    # Line 4
    if(not inputValidator(int(fourthArr[0]), 99, 0)):
        print("Line 4 dimension value must be in range 0-99")
        return False
    if(int(fourthArr[1]) != 4 and int(fourthArr[1]) != 8):
        print("Line 4 protocol number must be 4 or 8")
        return False
    if(not inputValidator(int(fourthArr[2]), 1000000, 1)):
        print("Line 4 max moves must be in range 1-1000000")
        return False
    # Line 6
    if(not inputValidator(int(sixthArr[0]), 99, 0)):
        print("Line 6 dimension value must be in range 0-99")
        return False
    if(not inputValidator(int(sixthArr[1]), 1000000, 1)):
        print("Line 6 max moves must be in range 1-1000000")
        return False
    if(not inputValidator(int(sixthArr[2]), 100000, 1)):
        print("Line 6 repetition value must be in range 1-100000")
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
    # declare all local variables that will be returned and used.
    lowestMoves = moves
    highestMoves = 0
    sumMoves = 0
    averageMoves = 0
    # this works because range() does not include the final number in the specified range.
    for n in range(numberSimulations):

        # This function outputs lowest number of moves, highest number of moves, and average number of moves.
        madeMoves = runSingleExperimentRepitition(dimension, protocol, moves)
        if(madeMoves < lowestMoves): lowestMoves = madeMoves
        if(madeMoves > highestMoves): highestMoves = madeMoves
        sumMoves += madeMoves
    # count up the moves made and get the average:

    averageMoves = sumMoves / numberSimulations # old way: calcAvg(averageMovesItems)
    return lowestMoves, highestMoves, averageMoves


# MAIN FUNCTION #

# Start statement:
print("This program is ment to simulate two people wondering in the woods!")
print("Imagine the two people are on a grid coordinate system.")
print("The two people lost in the woods are taking random turns to move in order to try and find the other person.")
print("The people are going to be trying to find eachother given different inputs of Grid Dimension, Maximum Moves, and Movement Protocol")
print("\tMovement Protocol 4 allows for movement in the four cardinal directions but fails to move when trying to move outside the grid.")
print("\tMovement Protocol 8 is like Movement Protocol 4 but allows for diagonal movement and reattempts a new move when trying to move outside of the grid.")
print("These different modifications to variables between runs will be called experiments.")
print("We will be running 3 of these experiments based on the input data given in the file indata.txt")
print("The simulations, in many cases, will be repeated multiple times for better accuracy of the results.")
print("\tNote, a simulation is one insteance of a random wondering test given a dimension, maximum number of moves, and movement protocol.")
print("\nRunning file validation...")

# The simulations, in many cases, will be repeated multiple times for better accuracy of the results.
# a simulation is one insteance of a random wondering test.

try:
    # opening file and validating input data
    fileIn = open("indata.txt", "r")
    fileOut = open("outdata.txt", "w")
except:
    print("File indata.txt could not be opened.")
    exit()

if(not validateFile(fileIn)):
    print("Invalid input file format. Please try again.")
else:
    fileIn.seek(0)
    
    print("File validated, running experiments...\n")

    ### EXPERIMENT 1 ###

    firstStr = fileIn.readline()
    firstArr = firstStr.split(',')
    secondStr = fileIn.readline()
    secondArr = secondStr.split(',')

    protocol = int(secondArr[0])
    maxMoves = int(secondArr[1])
    repetitions = int(secondArr[2])

    fileOut.write('Experiment 1 changes the dimensions of the grid. Other variables are held constant.\n')
    fileOut.write('-------------------------------------------------------------------------------------\n')
    fileOut.write('|           | Maximum   | Number of |           | Lowest    | Highest   | Average   |\n')
    fileOut.write('| DIMENSIONS| Moves     | Repeats   | Protocol  | Moves     | Moves     | Moves     |\n')
    fileOut.write('-------------------------------------------------------------------------------------\n')
    for dimensionStr in firstArr:
        dimension = int(dimensionStr)
        low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
        fileOut.write('| %10d| %10d| %10d| %10d| %10d| %10d| %10.3f|\n' % (dimension, maxMoves, repetitions, protocol, low, high, avg))

    fileOut.write('-------------------------------------------------------------------------------------\n\n')

     ### EXPERIMENT 2 ###

    thirdStr = fileIn.readline()
    thirdArr = thirdStr.split(',')
    fourthStr = fileIn.readline()
    fourthArr = fourthStr.split(',')

    dimension = int(fourthArr[0])
    protocol = int(fourthArr[1])
    maxMoves = int(fourthArr[2])

    fileOut.write('Experiment 2 changes the number of wanderings (repeats) for each row. Other variables are held constant.\n')
    fileOut.write('--------------------------------------------------------------------------------------\n')
    fileOut.write('| NUMBER OF |            | Maximum   |           | Lowest    | Highest   | Average   |\n')
    fileOut.write('| REPEATS   | Dimensions | Moves     | Protocol  | Moves     | Moves     | Moves     |\n')
    fileOut.write('--------------------------------------------------------------------------------------\n')

    for repetitionStr in thirdArr:
        repetitions = int(repetitionStr)
        low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
        fileOut.write('| %10d| %11d| %10d| %10d| %10d| %10d| %10.3f|\n' % (repetitions, dimension, maxMoves, protocol, low, high, avg))

    fileOut.write('--------------------------------------------------------------------------------------\n\n')

    ### EXPERIMENT 3 ###

    fifthStr = fileIn.readline()
    fifthArr = fifthStr.split(',')
    sixthStr = fileIn.readline()
    sixthArr = sixthStr.split(',')

    dimension = int(sixthArr[0])
    maxMoves = int(sixthArr[1])
    repetitions = int(sixthArr[2])

    fileOut.write('Experiment 3 changes the protocols.  Other variables are held constant.\n')
    fileOut.write('--------------------------------------------------------------------------------------\n')
    fileOut.write('|           |            | Maximum   |           | Lowest    | Highest   | Average   |\n')
    fileOut.write('| PROTOCOL  | Dimensions | Moves     | Repeats   | Moves     | Moves     | Moves     |\n')
    fileOut.write('--------------------------------------------------------------------------------------\n')

    for protocolStr in fifthArr:
        protocol = int(protocolStr)
        low, high, avg = runExperiments(dimension, protocol, maxMoves, repetitions)
        fileOut.write('| %10d| %11d| %10d| %10d| %10d| %10d| %10.3f|\n' % (protocol, dimension, maxMoves, repetitions, low, high, avg))

    fileOut.write('--------------------------------------------------------------------------------------\n\n')

    print("The Experiments have complete and the data has been output to the file \"indata.txt\"")
    print("Good-bye! Thank you for Experimenting! <(￣︶￣)>")
