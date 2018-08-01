# **********************************************************
# Assignment: Exercise 4: Variables and Names
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/30)
# Date Completed: (2018/07/30)
#
# Completion time: 45 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars avaliable")
print ("There are only", drivers, "drivers avaliable")
print ("There will be", cars_not_driven, "empty cars today")
print ("We can transport", carpool_capacity, "people today")
print ("We have", passengers, "to carpool today")
print ("We need to put about", average_passengers_per_car, "in each car today")

# Variables are capable of storing any form of information
# They can store numbers, phrases and symbols
# Variables can be used to create expressions and equations
# The software will use the most up to date value of the variable
# Variables cannot start with numbers or symbols; they must start with alphabets

# There is a difference between the = (single equal) and the == (double equal)
# The single equal (=), equates a value on the right to the variable on the left
# However, the double equal (==) is a boolean operator; it checks if both values on the sides equal each other

