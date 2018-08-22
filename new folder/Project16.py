# **********************************************************
# Assignment: Project 16: Password Generator
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
# Completion time: 2 hours 
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************
import random

password_list = []
uppercase_set = []
lowercase_set = []
symbols_set = []
choice_selector = []

numbers_set = [0,1,2,3,4,5,6,7,8,9]
uppercase_set.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase_set.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
symbols_set.extend("~`@#$%^&*()-_+=\|]}[{?/>.<,;:'")

number_of_passwords = int(input("How many passwords do you want generated? "))

length_counter = 0
character_selector = 0
type_selector = 0
password_counter = 1
character_selected = " "
password = " "

while password_counter <= number_of_passwords:
    password_length = int(input(f"What is the desired length of Password {password_counter}? "))
    lowercase_response = input (f"Would you like lowercase alphabets in Password {password_counter}? ").lower()
    uppercase_response = input (f"Would you like uppercase alphabets in Password {password_counter}? ").lower()
    numbers_response = input(f"Would you like numbers in Password {password_counter}? ").lower()
    symbols_response = input(f"Would you like symbols in Password {password_counter}? ").lower()

    if lowercase_response == "yes":
        choice_selector.append(1)
#       print(choice_selector)

    if uppercase_response == "yes":
        choice_selector.append(2)
#       print(choice_selector)

    if numbers_response == "yes":
        choice_selector.append(3)
#       print(choice_selector)

    if symbols_response == "yes":
        choice_selector.append(4)
#       print(choice_selector)
       
    if lowercase_response == "no" and uppercase_response == "no" and numbers_response == "no" and symbols_response == "no":
        print ("Okay, that was a nice try. But, who the hell do you think I am? Go back and retry kid.")
        continue
#   else:
#       print ("checK")'''

    while length_counter < password_length:
#       print ("1", choice_selector)
#       print ("2", type_selector)
        type_selector = random.choice(choice_selector)
#       print ("3",choice_selector)
#       print ("4",type_selector)
#       print("\n")

        if type_selector == 1:
            character_selector = random.randint(0,25)
            character_selected = lowercase_set[character_selector]
            password_list.append(character_selected)
#           print (character_selected)

        elif type_selector == 2:
            character_selector = random.randint(0,25)
            character_selected = uppercase_set[character_selector]
            password_list.append(character_selected)
#           print (character_selected)

        elif type_selector == 3:
            character_selector = random.randint(0,9)
            character_selected = numbers_set[character_selector]
            password_list.append(character_selected)
#           print (character_selected)

        elif type_selector == 4:
            character_selector = random.randint(0,29)
            character_selected = symbols_set[character_selector]
            password_list.append(character_selected)
#           print (character_selected)
        else:
            print ("Who do you think you are? Do you want a password or not? If not, then leave this program immediately!")
            break
        length_counter += 1

    password = ''.join(map(str, password_list))
    print(f"Password {password_counter}: {password} \n")
    choice_selector.clear()
    length_counter = 0
    password_list.clear()
    password_counter += 1

'''
    choice_selector.clear()
    type_selector = 0
    password = " "
    password_length = 0
    lowercase_response = " "
    uppercase_response = " "
    numbers_response = " "
    symbols_response = " "
    character_selector = 0
    character_selected = " "
    password_list.clear() '''


