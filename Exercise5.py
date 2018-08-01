# **********************************************************
# Assignment: Exercise 5: More Variables and Printing
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

# Everytime a double quote ("") is placed around text, it becomes a string
# A string is something that the program will actually use
# A string is typed, printed, shown, saved to files and sent to servers etc...
# The point is that a string is utilized as the program functions
# It is not an obselete part of the code

my_name = 'Aditya Sharma'
my_age = 18
my_height = 6 # Feet
my_weight = 145 # Pounds
my_eye_color = 'Dark Brown'
my_teeth_color = 'Whiteish Yellow'
my_hair_color = 'Black'

# As you can see above, variables are capable of storing strings 
# as values. Variables can store strings as values if the value is 
# surrounded by single quotes.

print (f"Lets talk about {my_name}") 
print (f"{my_name} is roughly {my_height} feet tall.")
print (f"{my_name} is also {my_weight} pounds")
print (f"He has {my_eye_color} colored eyes and {my_hair_color} hair.")
print (f"But, he has {my_teeth_color} teeth and that doesn't look good.")

# You don't need to seperate the strings with commas to enter 
# a variable value. You can format the entire string. This 
# tells the IDE to enter the inputted variable's value. 
# Add the 'f' before the quotations and surround the variable
# by curly brackets. This is known as


print ("Allow me to add all the numerical values: %d" %(my_weight + my_age + my_height))

# %s is used to substitute a value of a string
# %d is used to substitute a value of a digit (number)
# %f is used to substitute a value of a number, specifically a "float" number
# %r is used to represent anything. HOWEVER, if used for a string, it will put quotes around the substituted value.
# print ("If I were to add %d, %d, and %d, I would get %d" %(age, height, weight, age + height + weight))
# When you use %s or %d, the value of a variable is substituted into them
# The variables need to be mentioned afterwards in order.

# print ("My name is %s" % name)
# print ("The boy said that his name is %r" % name)
# Using %r for a string value will place quotations around the substituted string value





