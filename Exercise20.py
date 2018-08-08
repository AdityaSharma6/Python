# **********************************************************
# Assignment: Exercise 20: Functions and Files
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

from sys import argv

script, input_file = argv # When the program requires the user to input a specific file, import argv

def print_all(f):
    print (f .read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count, f .readline())

current_file = open(input_file)

print (f"First, let us print the contents of {input_file}.")
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("let's print three lines:")

'''
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file) '''

print (f"{f}")