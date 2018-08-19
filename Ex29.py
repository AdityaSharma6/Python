# **********************************************************
# Assignment: What If
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/06)
# Date Completed: (2018/08/06)
#
# Completion time: 40 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

people = 20
cats = 30
dogs = 15

number1 = 10
number2 = 10

if people < cats: # This is an if statement. The stuff below it only runs if the boolean expression evaluates to "True".
    print ("Too many cats! The world is doomed!")

if people > cats: # Since this expression is false, the code under it will not run
    print ("not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
print (dogs)

if people >= dogs:
    print("people are less than or equal to dogs")

if people == dogs:
    print ("People are dogs")

if number1 == number2:
    print ("Aditya is the best coder ever.")

