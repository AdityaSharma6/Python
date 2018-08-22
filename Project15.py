# **********************************************************
# Assignment: Project 15: Reverse Word Order
#
# Description: Write a program (using functions!) that asks
# the user for a long string containing multiple words. 
# Print back to the user the same string, except with 
# the words in backwards order.
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 5 minutes hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

user_string = input ("Input a phrase containing multiple words: ")
list1 = user_string.split(" ")

print ("\n", list1)
list1.reverse()
print ("\n", list1)

list2 = " ".join(list1)
print (list2) 
