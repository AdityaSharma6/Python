# **********************************************************
# Assignment: Project 4: Divisors
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 25 min
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("This program is known as Divisor!")
print ("Please input a number and I will find all the divisors for that number.")
print ("Enter the number here:", end = ' ')
number = int(input())
divisor = 1
list1 = []

while divisor <= number:
    remainder = number % divisor
    print (f"{number} % {divisor} = {remainder}")

    if remainder == 0:
        list1.append(divisor)
    
    divisor = divisor + 1

print (list1)


        
    

