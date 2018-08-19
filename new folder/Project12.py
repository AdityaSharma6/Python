# **********************************************************
# Assignment: Project 12: List Ends
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 5:45 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

list1 = []
number_of_elements = int(input("Input the number of elements in the list."))
counter = 0

while counter <= number_of_elements:
    number_added = int(input("Input a number you would like to have in the list."))
    list1.append(number_added)
    counter += 1

def function ():
    list2 = []
    list2.append(list1[0])
    list2.append(list1[(len(list1) - 1)])
    print (list2)

function()

