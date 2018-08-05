# **********************************************************
# Assignment: Exercise 11.1: Asking Questions: Custom Form
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

print (""" Hello there! We would like to get to know you better.
Is it okay if we ask you a series of questions? """, end = ' ') # The end = ' ' acts as a place holder. The next variable is automatically substituted into the current string on the same line.
Initiation_response = input ()

print ("What is you name?", end= ' ')
name = input ()

print ("How old are you?", end = ' ')
age = input ()

print ("Which educational institution do you currently attend?", end = ' ')
school = input ()

print ("And, which grade are you in?", end = ' ')
grade = input ()

# input () is a function which allows for user input
# The function allows for text, numerical and symbolic values to be inputted
