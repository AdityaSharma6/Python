# **********************************************************
# Assignment: Exercise 6.1: Strings and Text
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
person_A = "Bob"
person_B = "Aditya"

my_name = "Aditya"
number_of_males = 2
number_of_females = 5
adityas_family_size = 7
adityas_introductory_statement = f"There are {adityas_family_size} in my family"
adityas_more_detailed_introductory_statement = f"There are {adityas_family_size} members in my family. There are {number_of_males} males and {number_of_females} females in my family."


print (f"{person_A}: 'Hi! My name is Bob. What's your name?' ")
print (f"{person_B}: 'Hey! My name is Aditya. Nice to meet you bud. How many people are in your family?' {adityas_introductory_statement}")
print (f"{person_A}: 'Thats not detailed enough for me to reply. Retry.' ")
print (f"{person_B}: 'Well, if you say so. {adityas_more_detailed_introductory_statement}'")