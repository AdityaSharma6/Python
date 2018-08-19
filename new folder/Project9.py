# **********************************************************
# Assignment: Project 9: Guessing Game
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/010)
# Date Completed: (2018/08/12)
#
# Completion time: 2 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

import random # Importing something that allows for an otherwise unique function is known as a module

random_number = 0
user_guess = 1
exit_response = " "
counter = 0

while exit_response != "exit":
    counter += 1
    random_number = random.randint(1, 9)
    user_guess = 0
    print (random_number)

    while user_guess != random_number:
        
        user_guess = int(input("Input your guess: "))

        if user_guess < random_number:
            print ("Guess higher. You are TOO LOW.")
        elif user_guess > random_number:
            print ("Guess lower. You are TOO HIGH.")
        else:
            print ("Perfect! You are EXACTLY RIGHT.")
            exit_response = input ("To exit, input \"exit\". To continue, input anything else. ").lower()
            
            if exit_response == "exit":
                break
            else:
                continue
    

print (f"You have completed the game {counter} times.")
    
'''
user_guess = 0
continuation = "yes"

 continuation != "yes":
    random_number = random.randint(1,9)
    print (random_number)


    while user_guess != random_number:

        user_guess = int(input("Guess a number that is between 1 and 9: "))
        if user_guess < random_number:
            print ("Guess higher. You are TOO LOW.")
        elif user_guess > random_number:
            print ("Guess lower. You are TOO HIGH.")
        else:
            print ("Perfect! You are EXACTLY RIGHT.")
            continuation = input("If you would like to exit, type \"exit\". If not, enter anything else. ").lower()
            if continuation == "exit":
                break 
            else:
                user_guess = 0
                continue '''



    





