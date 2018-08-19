# **********************************************************
# Assignment: Project 2: Odd or Even
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 10 min
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("Welcome, this is a program that determines whether the number you have inputted is odd or even.")
number = input("Please submit an integer number: ")

list1 = []
list1.extend(number)
print (list1)

list1.reverse()
print (list1)

x = int(list1 [0])
print (x)

if x == 0 or x==2 or x==4 or x==6 or x==8:
    print("The integer you submitted is even!")
else:
    print("The integer you submitted is odd!")

