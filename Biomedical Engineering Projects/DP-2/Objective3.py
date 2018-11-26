# **********************************************************
# Assignment: Objective 3
#
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************
import math 

'''
teamNumber = 17
bodyWeight =            # Weight in newtons
outerDia =              # Outer diameter of the femoral diaphysis (femoral shaft)
canalDiameter =         # Diameter of the medullary canal
canalOffset =           # The offset between teh center of the femoral head and the center of the medullary canal
modulusBone =           # Modulus of elasticity of cortical bone in gigapascals
ultTenStrength =        # Ultimate tensile strength
modulusImplant =        # Modulus of elasticity of implant material in gigapascals
stemDia =               # Diameter of implant stem
'''

# Subprogram 1 Variables
bodyWeight = 100
canalDiameter = 10
minStemDia = 20 
appTenStress = 30
ultTenStrength = 40


def subprogram_one (): # Calculates the minimum allowable implant stem diameter by assuming a combined loading scenario.
    print ("Subprogram 1 Running... \n")

    force = 3.5 * bodyWeight
    stemDiameter = 0.5 * canalDiameter
    stemRadius = 0.5 * stemDiameter
    crossSectionalArea = math.pi * math.pow(stemRadius,2)
    axialStress = force / crossSectionalArea
    # axialStress = appTenStrength

    print (force)
    print (stemDiameter)
    print (stemRadius)
    print (crossSectionalArea)
    print (axialStress)

    print (f"bodyweight = {bodyWeight} \ncanalDiameter = {canalDiameter} \nultTenStrength = {ultTenStrength} \nminStemDia = {minStemDia} \nappTenStress = {appTenStress}")
    # Last task remaining is to optimize the equation to find the minimum stem diameter

def subprogram_two():
    

def subprogram_three():
    print ("hi")

def exit_program():
    print ("hi")


def main ():
    print ("Select a number which corresponds to the choice that you want to select. \nIf you want to run Subprogram 1, type '1'.")
    user_input = input("1. Subprogram 1\n2. Subprogram 2\n3. Subprogram 3\n4. Exit from program")

    if (user_input == "1"):
        subprogram_one()

    elif (user_input == "2"):
        subprogram_two()

    elif (user_input == "3"):
        subprogram_three()

    elif (user_input == "4"):
        exit_program()

main()


