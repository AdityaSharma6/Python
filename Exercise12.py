# **********************************************************
# Assignment: Exercise 12: Prompting People
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 20 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

# Previously, we learned that the input () function was used for user input
# Now, you can use the same function to act as a prompt so the user knows what to input

y = input (" What is you name? ")

# This allows us to eliminate the need for a print statement that we previously implemented to ask a question

age = input (" How old are you? ")
grade = input (" Which grade are you in? ")
school = input (" Which educationla institution do you currently attend? ")
program = input (" Are you in a specialized education program? ")
comment_weight = input (" You look a bit ... plump. How much do you weigh? ")

print (f"So, let me get this correct. Your name is {y}, you're in {grade} in {school} and you're in the {program}. Right? Also, I'm sorry for asking about your weight, but you looked like you weighed more than {comment_weight}")
