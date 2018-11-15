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

'''
for counter in range (2000, 3201):
    number = counter

    if (number%7 == 0) and (number%5 != 0):
        print (number)
'''

# I will modify the code by providing the user with the freedom to determine the range, multiple and other values.

'''
max_value = int(input("Enter the maximum integer value: "))
min_value = int(input("Enter the minimum integer value: "))

def function (max_value, min_value):

    for counter in range(min_value, max_value):
        number = counter

        if (number%7 == 0) and (number%5 != 0):
            print (number)

function(max_value, min_value)
'''

max_value = int(input("Enter the maximum integer value: "))
min_value = int(input("Enter the minimum integer value: "))
divisible = int(input("Enter a value that the integer should be divisble by: "))
not_divisible = int(input("Enter a value that the integer should not be divisible by: "))


def function (max_value, min_value, divisible, not_divisible) :

    for counter in range(min_value, max_value):
        number = counter

        if (number%divisible == 0) and (number%not_divisible != 0):
            print (number)

function(max_value, min_value, divisible, not_divisible)







