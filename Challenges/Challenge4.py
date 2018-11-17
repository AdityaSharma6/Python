# **********************************************************
# Assignment: Challenge 4
#
# Description: Question:
# Write a program which accepts a sequence of comma-separated 
# numbers from console and generate a list and a tuple which 
# contains every number. Suppose the following input is 
# supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Author: Aditya Sharma
#
# Date Start: (2018/11/17)
#
# Completion time: 10 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************
'''
value = input("Enter a set of values seperated by a comma: ")
list1 = [value]

tuple1 = (value.split(","))
print (list1)
print(tuple1)

'''
values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)
