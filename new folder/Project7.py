# **********************************************************
# Assignment: Project 7: List Comprehensions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/010)
# Date Completed: (2018/08/12)
#
# Completion time: 12 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

import random
# List Comprehension is the process of making code more compact when conducting tasks involving lists
# Let User Define How many lists
# Let User Define the length of each list
# Specifiy the max and min values for each list
# Randomly generate values for each list
# Seperate even values from each list and store in a new list
# Seperate odd values from each list and store in a new list

print ("How many lists would you like to make?", end = ' ')
number_of_lists = int(input())
counter = 0
master_list = []
odd_list = []
even_list = []

def function1 ():
    counter = 0
    while counter < number_of_lists:
        print (f"What would you like to name List {counter}? ", end = ' ')
        list_name = input ()
        master_list.append([])

        number_of_elements = int(input(f"How many values would you like \"{list_name}\" to have? "))
        element_counter = 0

        max_value = int(input(f"Input {list_name}'s max potential value: "))
        min_value = int(input(f"Input {list_name}'s min potential value: "))

        while element_counter < number_of_elements:
            random_value = random.randint(min_value, max_value)
            master_list[counter].append(random_value)
            element_counter += 1 

            if (random_value % 2) == 0:
                even_list.append(random_value)
            else:
                odd_list.append(random_value)
        counter += 1

function1()
print(odd_list)
print(even_list)
print(master_list)







