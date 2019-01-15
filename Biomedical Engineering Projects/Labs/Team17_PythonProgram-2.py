# DP-2 Python Program
# Team 17
# December 5th, 2018
# Subprogram 1,3 and menu by Bardia Sedighi
# Subprogram 2 by Jenn Ward

import math

def subprogram1(bodyWeight, ultTenStrength, canalOffset, canalDiameter):
    """
     A function that calculates the minimum implant stem diameter; which is the diameter when the applied tensile
    stress is equal to the ultimate tensile strength of the material being used in the implant

    :param bodyWeight: float, the weight of the patient
    :param ultTenStrength: int, the ultimate tensile strength of the implant material
    :param canalOffset: int, the offset between the centre of the femoral head and the centre of the Medullary Canal
    :param canalDiameter: int, the diameter of the Medullary Canal
    """
    force = 3.5 * bodyWeight
    moment = force * canalOffset
    minStemDia = canalDiameter  # initializing minStemDia with the value of the canal diameter
    step = -0.0001  # step is chosen to be -0.0001 so that our answer is more accurate

    while True:
        appTenStress = (-4 * force) / (math.pi * minStemDia ** 2) + (
                    (64 * moment * 0.5 * minStemDia) / (math.pi * minStemDia ** 4))
        # equation for axial stress = force/area
        # equation for bending stress = My/I
        # We assume the applied tensile stress acting on the bone is a function of both axial and bending stress
        if appTenStress > ultTenStrength:
            # if the applied tensile stress is bigger than the Ultimate tensile strength the implant fails
            break
        minStemDia += step   # adds the step to the diameter each time the condition is false

    minStemDia -= step  # subtracts the value of the diameter that caused failure from the step
                        # in order to give the minimum allowable diameter

    print("")
    print("Output:")
    print("Body weight = ", round(bodyWeight, 0), "N")
    print("Canal Diameter = ", canalDiameter, "mm")
    print("Ultimate Tensile Strength = ", ultTenStrength, "MPa")
    print("Minimum Implant Stem Diameter: ", round(minStemDia, 2), "mm")
    print("Applied Tensile Stress = ", round(appTenStress, 0), "MPa")
    print("----------------")
    print(" ")
    print(" ")


def subprogram2(bodyWeight,teamNumber,filename):
    """
    A function that calculates the fatigue life of the the implant and the stress amplitude corresponding to failure

    :param bodyWeight: float, the weight of the patient
    :param teamNumber: int, the team number of our group
    :param filename: the name of the file being read
    """
    data_points = open(filename, 'r')   # importing data from a file
    points = data_points.readlines()    # returning each line from the file as an item in a list
    data_points.close()
    data_split = []                     # initializing the list data_split
    for line in points:
        data_split.append(line.split())   # splitting each item in points and adding it to data_split

    stress = []                         # initializing the list stress
    cycles_to_failure = []              # initializing the list cycles_to_failure

    for i in range(len(data_split)):
        stress.append(float(data_split[i][0]))  # adding the first value of data_split(stress values) to stress
        cycles_to_failure.append(int(data_split[i][1]))  # adding the second value of data_split(cycle values) to stress

    stemDia = float(input("Please Enter the diameter of the implant in mm: "))
    if stemDia <= 0:    # diameter cannot be 0 or negative 
        print(" ")
        print("Invalid input")
        print("----------------")
        print(" ")
        return
    force = 10 * bodyWeight
    area = (math.pi / 4) * (stemDia ** 2)  # assume implant is solid cylinder
    max_stress = force / area
    min_stress = -force / area
    stress_amplitude = (max_stress - min_stress) / 2

    for i in range(len(cycles_to_failure)):
        stress_factor = 6 + math.log(cycles_to_failure[i], 10) ** (teamNumber / 30)
        adjusted_amplitude = stress_factor * stress_amplitude
        if adjusted_amplitude > stress[i]:  # checking to see if the adjusted amplitude is bigger
                                            # than the corresponding stress value
            cyclesFail = cycles_to_failure[i]
            stressFail = adjusted_amplitude
            print("")
            print("Output:")
            print("Number of Cycles = ", cyclesFail, "Cycles")
            print("Maximum Stress Amplitude = ", round(stressFail, 2), "MPa")

            print("----------------")
            print(" ")
            print(" ")
            return
    print(" ")
    print("Infinite cycles without Failure!!")
    print("----------------")
    print(" ")
    print(" ")
    

def subprogram3(modulusBone,modulusImplant,bodyWeight,outerDia,canalDiameter):
    """
    A function that calculates the number of years post-implantation before there is a risk of femoral fracture based on
    the reduced compressive stress acting on the bone.

    :param modulusBone: int, modulus of elasticity of cortical bone
    :param modulusImplant: int, modulus of elasticity of the implant material
    :param bodyWeight: float, the weight of the patient
    :param outerDia: int, the outer diameter of the femoral diaphysis
    :param canalDiameter: int, the diameter of the Medullary Canal
    """
    force = 30 * bodyWeight
    compressive_stress = -4 * force / (math.pi * (outerDia ** 2 - canalDiameter ** 2))  # assume bone is hollow cylinder
    stressReduc = compressive_stress * math.sqrt((2 * modulusBone) / (modulusBone + modulusImplant))
    Eratio = math.sqrt(modulusImplant/modulusBone)
    years = 0   # initializing years
    y = 0.001 * (years ** 2) - 3.437 * Eratio * years + 181.72  # relationship between compressive strength of bone and
                                                                # number of years since implantation

    bone_stress = abs(stressReduc)  # reduced stress being applied is negative but we need the absolute value

    while bone_stress < y:  # checking to see when the reduced stress is greater than the bone strength
        years += 1      # adding 1 to years each time the bone strength is bigger than the reduced stress
        y = 0.001 * (years ** 2) - 3.437 * Eratio * years + 181.72

    yrsFail = years - 1  # we want exactly one year before the implant fails
    stressFail = 0.001 * (yrsFail ** 2) - 3.437 * Eratio * yrsFail + 181.72

    if yrsFail < 0:  # cannot have negative years before failure
        print("")
        print("Output:")
        print("Number of Years before Fracture Risk = ", 0, "Years")
        print("Compressive Stress on Bone corresponding to Failure= ", round(stressFail, 2), "MPa")
        print("----------------")
        print(" ")
        print(" ")
        return

    print("")
    print("Output:")
    print("Number of Years before Fracture Risk = ", yrsFail, "Years")
    print("Compressive stress on Bone corresponding to Failure= ", round(stressFail, 2), "MPa")
    print("----------------")
    print(" ")
    print(" ")


def main():
    """
    The main function executes the menu of the program. It takes the user input and
    runs the subprogram initiated by the user.
    """
    teamNumber = 17
    bodyWeight= 85*9.81
    outerDia = 31
    canalDiameter = 17
    canalOffset= 47
    modulusBone= 17  # Milestone 4 Specification Sheet
    ultTenStrength = 950  # Titanium Alloy (Ti6AL4V)
    modulusImplant= 114  # Titanium Alloy (Ti6AL4V)
    stemDia= canalDiameter
    filename = "SN Data - Sample Metal.txt"

    isRunning = True
    while isRunning:
        print("Program Menu:")
        print("1. Sub Program 1")
        print("2. Sub Program 2")
        print("3. Sub Program 3")
        print("4. Exit")
        print(" ")
        subP = input("Please select the program that you want to run: ")
        if subP == "1":
            subprogram1(bodyWeight, ultTenStrength, canalOffset, canalDiameter)
        elif subP == "2":
            subprogram2(bodyWeight,teamNumber, filename)
        elif subP == "3":
            subprogram3(modulusBone, modulusImplant, bodyWeight, outerDia, canalDiameter)
        elif subP == "4":
            isRunning = False
            print("Thank You for using our Program")
        else:
            print("Sorry, Your Input is Invalid")
            print("")


main()
