# **********************************************************
# Assignment: 1st Project: Age
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 10 min
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("What is your name?", end = ' ')
name = input ()

print ("Currently, how old are you?", end = ' ')
age = int(input())

years = 2018 + (100 - age)
print (f"You will become 100 years old by {years}.")