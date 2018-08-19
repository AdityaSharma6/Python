# **********************************************************
# Assignment: Project 5: List Overlap
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/09)
# Date Completed: (2018/08/09)
#
# Completion time: 3 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************
import random

print ("How many elements should list1 have? Enter your response as an integer: ", end = ' ')
list1_size = int(input())
print ("How many elements should list2 have? Enter your response as an integer: ", end = ' ')
list2_size = int(input())
print ("\n")


list1 = []
list1_max_value = int(input("Maximum value to be in List1: "))
list1_min_value = int(input("Minimum value to be in List1: "))
print ("\n")

list2 = []
list2_max_value = int(input("Maximum value to be in List2:  "))
list2_min_value = int(input("Maximum value to be in List2:  "))
print ("\n")

list3 = []


for a in range(0,list1_size):
    number = random.randint(list1_min_value, list1_max_value)
    list1.append(number)

for b in range(0, list2_size):
    number = random.randint(list2_min_value, list2_max_value)
    list2.append(number)


'''
if list2_size > list1_size:
    print ("List2 has more entries than List1.")
    print ("I will increase the number of entries within List1 to match that of List2.")
    print ("The additional entries will be blanks or 0's.")
    difference = list2_size - list1_size

    for elements1 in range (0, difference):
        list1.append(0)

    print (f"List2 has recieved {difference} extra 0's")


elif list1_size > list2_size:
    print ("List1 has more entries than List2.")
    print ("I will increase the number of entries within List2 to match that of List1.")
    print ("The additional entries will be blanks or 0's.")
    difference = list1_size - list2_size 

    for elements2 in range (0, difference):
        list2.append(0)

    print (f"List2 has recieved {difference} extra 0's")
    '''

list1.sort()
list2.sort()
print (list1)
print (list2)
print ("\n")

largest_number_index_value = len(list1)
largest_number = list1 [largest_number_index_value - 1]
smallest_number = list1 [0]
counter = smallest_number

while counter <= largest_number:
    if counter in list1:
        if counter in list2:
            list3.append(counter)
    counter = counter + 1

list3.sort()
print (list1)
print (list2)
print (list3)


list3_length = len(list3)
list3_largest_number = list3 [list3_length - 1]
counter = -1


while counter <= list3_largest_number:
    counter = counter + 1

    if counter >= list3_length:
        break
    
    number_of_times_in_list2 = list2.count(list3[counter])
    number_of_times_in_list1 = list1.count(list3[counter])
    print (f"The number {list3[counter]} shows up {number_of_times_in_list1} times in List1.")
    print (f"The number {list3[counter]} shows up {number_of_times_in_list2} times in List2.")

print ("This is the end of the program. Be grateful you spoilt brat, this took my master 3 hours to build. Good Bye!")




    
