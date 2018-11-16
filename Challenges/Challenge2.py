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
# Completion time: 30 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************

number = 8
factorial = 1

for i in range(1, (number+1)):
    
    factorial = factorial * i

print (factorial)

