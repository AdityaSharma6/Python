# **********************************************************
# Assignment: Challenge 1
#
# Description: Question:
# Write a program which will find all such numbers which 
# are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
#
# Author: Aditya Sharma
#
# Date Start: (2018/11/14)
#
# Completion time: 30 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************

for counter in range (2000, 3201):
    number = counter

    if (number%7 == 0) and (number%5 != 0):
        print (number)






