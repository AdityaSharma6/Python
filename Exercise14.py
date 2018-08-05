# **********************************************************
# Assignment: Exercise 14: Prompting and Passing
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 45 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

from sys import argv # You are importing certain functions into your script (code)

script, user_name = argv # Here, you are unpacking the function "argv" into two variables known as script and User_name

# Again, variables that store strings need to have their text within either of the 2 forms of quotations
# Variables storing numbers do not need quotations
prompt = '< '
lives_rule = "Text Response ONLY: "
likes_rule = "Don't say anything that would make either of us feel uncomfortable. "


print (f"Hi {user_name}, I am the {script} script.") # Formatting & variable substitution
print ("I would like to ask you a few questions.")
print (f"Do you like me {user_name}") 
likes = input (prompt + likes_rule) 
# Since both variables store the 
# same data type, the addition sign can be used to concatenate 
# (join the values) the variables

print (f"Where do you live {user_name}")
lives = input(prompt + lives_rule) 
# This is another example of how the input function is being used. 
# It will display whatever is within its brackets and then will 
# provide the user with the opportunity to respond.

print ("What kind of computer do you have?")
computer = input (prompt) 

print (f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice. 
""")
response = input ("How was your day?... Please respond...")
# As explained previously, the input function will display what it needs
# to display and then will provide the user with an opportunity to respond.
# It is useful for prompts or to retrieve additional information from the
# user.

# The end = ' ' can only be used in a print statement when you want 
# the inputted value to be displayed on the same line as the printed
# statement. It cannot be used as you ask for the prompt.

# Add the "end = ' ' " to line 51 if you want to check.