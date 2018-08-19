# **********************************************************
# Assignment: Project 13: Fibonacci
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 9:15 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

repititions = int(input("How many numbers from the sequence would you like to have printed? "))

list1 = [0,1]
counter = 0

while counter < repititions:
    list1.append((list1[counter+1]) + (list1[counter]))
    counter += 1

del list1[0]
print(list1)

