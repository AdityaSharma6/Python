# **********************************************************
# Assignment: Challenge 2
#
# Description: Question:
# Write a program which can compute the factorial of a given
# numbers. The results should be printed in a comma-separated
# sequence on a single line.
#
# Author: Aditya Sharma
#
# Date Start: (2018/11/16)
#
# Completion time: 2 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************

'''
number = 8
factorial = 1

for i in range(1, (number+1)):
    factorial = factorial * i
print (factorial)
'''

number = int(input("Enter an integer value whose factorial you would like to find: "))
iteration = int(input("Enter the number of times you want the factorial function to repeat" ))

# There are variables within this function. 
# The variables within this function are in a different space. 
# Thus, these variables do not exist outisde this function. 
# Attempting to call them outside the function is pointless. 

def function(number, iteration): 
    counter = 1
    factorial = 1

    # While loops require a counter an it will start from the value assigned to the counter.
    while counter <= iteration:
        factorial = factorial * number
        number = number - 1
        counter += 1
    return factorial 

print (function(number, iteration))


