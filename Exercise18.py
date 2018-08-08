# **********************************************************
# Assignment: Exercise 18: Names, Variables, Code and Functions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 120 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

# Functions can do 3 things:
''' They name pieces of code the way variables name strings and numbers
    They take arguements the way your scripts take argv
    Using 1 and 2, they let you make your own "mini-script" or "tiny commands"
    A function can be created by using the command "def" '''

# A function is created by using the command "def"

def print_two (*args): 
    arg1, arg2 = args # The word args is unpacked into two variables
    print (f"arg1: {arg1}, arg2: {arg2}") # The two variables are printed. 

def print_two_again (arg1, arg2):
    print (f"arg1: {arg1}, arg2: {arg2}")

def print_one (arg1):
    print (f"arg1: {arg1}")

def print_none ():
    print ("I got nothing")

print_two ("Aditya", "Shaw") # He defined and gave the arguements values
print_two_again ("Zed", "Shaw")
print_one ("The End")
print_none() 

# The system ran through the entire piece of code and printed out the values for the arguements

