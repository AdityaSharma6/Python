# **********************************************************
# Assignment: Exercise 11: Asking Questions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 20 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************
name = "Aditya" # String variables need to have quotations
grade = 19 # Numerical values being stored do not need to have quotations

print ("How old are you?", end= ' ') # The end = ' ', is a function. It acts as a placeholder for the input. It ensures that the inputted value is displayed on the same line and not on the next line. 
age = input ()
print ("How tall are you?", end= ' ')
height = input ()
print ("How much do you weigh?", end= ' ')
weight = input()

print (f"So, your name is {name}. You are {age} years old, are {height} feet tall and weigh {weight} pounds. Correct? {grade}")

