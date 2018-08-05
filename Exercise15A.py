# **********************************************************
# Assignment: Exercise 15.1: Reading Files
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

from sys import argv # This imports a file into the script which allows for user control

script, filename = argv # It mentions 1 variable which the user can directly specify from the terminal/ command line

txt = open(filename)

print (f"Here is your file: {filename}")
print(txt.read()) # First, it prints the variable "txt" which has the string (the filename) attached. Then the other command, .read() processes and displays the content from the file.

'''
print ("Type the filename again.")
file_again = input ("> ")

txt_again = open(file_again)
print(txt_again.read())
'''