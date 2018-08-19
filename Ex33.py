# **********************************************************
# Assignment: Exercise 33: While Loops
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 11:30 -
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

i = 0
numbers = []

def function1 ():
    while i < x:
        print (f"The value of \"i\" is: {i}")
        numbers.append(i)
        i = i + 1 # This is a counter. It needs to be placed at the end of each while loop so that the loop doesn't run for infinity

print ("Numbers now: ", numbers)
print (f"At the bottom i is {i}")

print ("The numbers: ")

for num in numbers:
    print (num)

