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

opened_file = open(filename) 
# The function "open()" simply opens up the file. It doesn't read or process the information within the file.

print (f"Here is your file: {filename}")

read_file = opened_file.read()
print(read_file + "\n") 


file_again = print ("Type the filename again: ", end = ' ') 
file_again = input ()

# file_again = input ("Type the filename again: ")

txt_again = open(file_again)
print(txt_again.read())
