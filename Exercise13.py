# **********************************************************
# Assignment: Exercise 13: Parameters, Unpacking, Variables
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 45 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print (f"The script is called: {script}")
print (f"Your first variable is: {first}")
print (f"Your second variable is: {second}")
print(f"Your third variable is: {third}")
 
# By importing in the beginning, you are bringing in a different set of commands
# The argv command lets the user define certain variable values.


