# **********************************************************
# Assignment: Project 18: Cows and Bulls
#
# Description: Write a password generator in Python. Be 
# creative with how you generate passwords - strong passwords 
# have a mix of lowercase letters, uppercase letters, numbers,
# and symbols. The passwords should be random, generating a 
# new password every time the user asks for a new password. 
# Include your run-time code in a main method.
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 5 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************

import random

number_list = ['0','1','2','3','4','5','6','7','8','9']
random_number = []
counter = 0
user_guess = 0
user_guess_list = []
user_counter = 0
cows = 0
bulls = 0

while counter < 4:
    random_index_number = random.randint(0,9)
    random_number.append(number_list[random_index_number])
    counter += 1

print (random_number)

user_guess = input("Input a 4 digit number: ")
user_guess_list.extend(user_guess)
print (user_guess_list)

while user_counter < 4:
    if (user_guess_list[user_counter]) == (random_number[user_counter]):
        cows += 1
        if (user_guess_list[user_counter]) in random_number:
            bulls += 1
    elif (user_guess_list[user_counter]) in random_number:
        bulls += 1
    user_counter += 1

print (cows)
print (bulls)




    