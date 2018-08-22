# **********************************************************
# Assignment: Project 14: List Remove Duplicates
#
# Description: Write a program (function!) that takes a list 
# and returns a new list that contains all the elements of 
# the first list minus all the duplicates.
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

import random
list0 = []
list2 = []
number_of_elements = int( input("Number of elements? "))
max_value = int(input("Max Number? "))
min_value = int(input("Min Number? "))
random_number = random.randint(min_value, max_value)
counter = 0

while counter <= number_of_elements:
    random_number = random.randint(min_value, max_value)
    list1.append(random_number)
    counter += 1
    
list1 = list0.copy()
index_counter = 0
list1.sort()
eliminations = 0

while index_counter < (number_of_elements - eliminations):
    shows_up = list1.count(list1[index_counter])
    if shows_up > 1:
        counter = 1
        while counter < shows_up:
            list1.pop(index_counter)
            counter += 1
            eliminations += 1
    index_counter += 1

list2 = list1.copy()
print(list2)