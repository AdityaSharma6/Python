# **********************************************************
# Assignment: Exercise 6: Strings and Text
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

types_of_people = 10 # Variable assigns a digit as the value
x = f"There are {types_of_people} types of people" # This is a variable that is a string which contains another variable whose value will be substituted in.

binary = "binary" # This is a string variable
do_not = "don't" # This is also a string variable
y = f"Those who know {binary} and those who {do_not}" # This is a variable that has two values to be substitued in

print (x) # This is a print statement that will print the variable. The variable that it will print has 1 value that needs to be substituted in.
print (y)

print (f"I said: {x}")
print (f"I also said: '{y}'")

hilarious = False # This is a boolean variable.
joke_evaluation = "Isn't that joke so funny?! {}" # This is a variable that has a undefined variable within. That variable's value will be defined when it is printed.
print (joke_evaluation. format(hilarious))

w = "This is the left side of... \n"
e = " \n a string with a right side."
print (w + e) # This is a print statement which is concatenating two variables that have string values. Since, it is being joined by the addition sign, there will be no space between both values.

# The value of variables can be added together to produce something new
# If the variables store strings (letters), they can be added together
# to produce a brand new sentence.

# Variables can be added into a phrase by using curly brackets
# and typing the name of the variable within the curly brackets.

# If the curly brackets are left empty, then you use ". format()" to 
# insert what you need to and the system will add it.

# When talking about strings nand the print function, concatenation is involved
# concatenation is the combination of things. You can use the "+" or the
# "," to concatenate. However, you can only use "+" if they are the
# same data type. Use commas to be on the safer side.





