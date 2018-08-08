# **********************************************************
# Assignment: Exercise 19: Functions and Variables
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 30
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

def cheese_and_crackers(cheese_count, boxes_of_crackers): # In the function, you have created 2 different variables.
    print (f"You have {cheese_count} cheeses!") # You print the variable's value
    print (f"You have {boxes_of_crackers} boxes of crackers!") # Again, you print the variable's value
    print ("Man, that's enough for a party!")
    print ("Get a blanket. \n") # You can include the escape functions on the same line

''' When you create a function, the following lines are indented. 
This is because it means that the following lines are all within the function.
The next time that the function is simply written as a piece of code, it will run.
Whatever the following lines of code say, the function will execute and run them. '''

print ("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30) # You can store values to the variables within the function anywhere.

print ("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
cheese_and_crackers(0, 0)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too: ")
cheese_and_crackers (10 + 20, 5 + 6) # When you create a function that has variables, the function will only run if it has values for its variables. Now, you can conduct mathematical operations within the function to change the values of the variables.

print ("And, we can also combine the variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000) # You can also do math with variables within the function.

# REMEMBER THAT THE FUNCTION WILL ONLY RUN IF IT HAS VALUES

