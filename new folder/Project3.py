# **********************************************************
# Assignment: Project 3: List Less Than 10
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 45 min
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("Welcome! How many numbers would you like to input?", end = ' ')
element_number = int(input())

list1 = []
list2 = []
list3 = []

for elements in range(0,element_number):
    print ("What number would you like to input?:", end = ' ')
    number = int(input())
    list1.append(number)
print ("\n" + "\n")


for elements in list1:
    if elements < 5:
        list2.append(elements)

list2.sort()
print ("This is a list that contains all the numbers less than 5:", list2)
print ("Would you like to continue with this exercise?:", end = ' ')
response1 = input().lower()

if response1 == "yes":
    print ("Please enter a number. The number will act as a benchmark and I will return values less than that number. Enter the number:", end = ' ')
    benchmark = int(input())

    for elements in list1:
        if elements < benchmark:
            list3.append(elements)

    list3.sort()
    print(list3)

else:
    print("Program is complete! Have a nice day!")




