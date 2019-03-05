# Name: Aditya Sharma, Abdullah Abdullah
# MacID: shara24, abdula39
# Student Number: 400189221, 400181288
# Date: March 4th 2019

def gearRatio (level1, level2): #Accepts lists as arguements. Lists correspond to series of Pitch Diameters
    #12, 18 - Idler, 36
    #12, 13, 13, 20
    # Thumb: 20, 20
    gearRatio1 = level1[2] / level1[0]
    gearRatio2 = level2[3] / level2[0]
    totalGearRatio = gearRatio1 * gearRatio2
    return totalGearRatio

def calculateSpeed(inputSpeed, totalGearRatio): # Calculates the output speed
    outputSpeed = inputSpeed / totalGearRatio
    return outputSpeed

def centerDistance(pitchDiameter): #Computes center distance of the gear train
    inputGearRadius = pitchDiameter[0]/2
    outputGearRadius = pitchDiameter[len(pitchDiameter) - 1]/2

    idlerSum = 0
    for i in range(1, len(pitchDiameter) - 1): # The loop ignores the first and last values of the list and gets the total sum of all the values in between.
        idlerSum = idlerSum + pitchDiameter[i] # This sum is the sum of all the diameters of the idler gears
    
    centerDistanceValue = inputGearRadius + outputGearRadius + idlerSum
    return centerDistanceValue    

def check_calculations(inputSpeed, level1, level2): # The function's main purpose is to essentially compare the assigned values to the calculated values
    assignedGearRatio = 45/9
    assignedOutputSpeed = 9
    assignedLevel1CenterDistance = 42
    assignedLevel2CenterDistance = 42

    calculatedGearRatio = gearRatio(level1, level2)
    calculatedOutputSpeed = calculateSpeed(inputSpeed, gearRatio(level1, level2))
    calculatedLevel1CenterDistance = centerDistance(level1)
    calculatedLevel2CenterDistance = centerDistance(level2)
    

    if (assignedGearRatio == calculatedGearRatio):
        print("GEAR RATIO TEST PASSED")
    else:
        print("GEAR RATIO TEST FAILED")
    
    if (assignedOutputSpeed == calculatedOutputSpeed):
        print("OUTPUT SPEED TEST PASSED")
    else:
        print("OUTPUT SPEED TEST FAILED")
    
    if (assignedLevel1CenterDistance == calculatedLevel1CenterDistance):
        print("FIRST LEVEL CENTER DISTANCE TEST PASSED")
    else:
        print("FIRST LEVEL CENTER DISTANCE TEST FAILED")

    if (assignedLevel2CenterDistance == calculatedLevel2CenterDistance):
        print("SECOND LEVEL CENTER DISTANCE TEST PASSED")
    else:
        print("SECOND LEVEL CENTER DISTANCE TEST FAILED")

    
check_calculations(45, [12,18,36], [12,13,13,20])

''' 
Reflection:
1) We can alter our program to accomodate for an unexpected data type in several ways.
One of the simpliest ways would be to do the following.

First, set up a loop that would run till infinity (While True:)

Second, collect user input and assign them to a variable instead of immediately
assigning them to be the arguements in the function. 

Third, in the while true loop, set up an two if statements that compare the data types
of the user's input to exemplar inputs to ensure that they are the same data type. If 
they are the same data type, break out of the while True loop and continue to the function.
If they are not the same data type, then you restart the while True loop and ask for the
input again. This repeats until the user gets the correct data type.

'''