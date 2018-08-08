# **********************************************************
# Assignment: Exercise 21: Functions Can Return Something
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 30
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

def add(a, b): # Tells the system that a funciton is being created and sets two variables
    print(f"Adding {a} + {b}") # It is a print statement which prints the value of the variables whilst indicating that they will be added
    return a + b # This stores the answer from this function

def subtract (a, b):
    print (f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a, b):
    print (f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print (f"DIVIDING {a} / {b}")
    return a / b

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")





'''
print ("Initiate Addition")

def addition ():
    print ("This is the function which results in addition")
   
    number1 = float(input("What is your first number: "))
    number2 = float(input("What is your second number: "))  

    sum = (number1 + number2)
    print (f"{number1} + {number2} = {sum}")
    
    print ("You have just ran the addition funtion. Continuing... \n \n \n")

def subtraction ():
    print ("This is the function which results in subtraction. \nInitiating subtraction sequence...")
    
    number1 = float(input("What is your first number: "))
    number2 = float(input("What is your second number: "))
    difference = number1 - number2
    
    print (f"{number1} - {number2} = {difference} ")

    print ("You have just ran the subtraction function. Continuing \n \n \n")

def multiplication():
    print ("This is the function for multiplication.")
    
addition()
subtraction() '''
