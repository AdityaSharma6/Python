# **********************************************************
# Assignment: Exercise 35: Branches and Functions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/07)
# Date Completed: (2018/08/07)
#
# Completion time: 11:30 -
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************
'''
from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")
    choice = input("> ")
    if "0" in choice or "1" in choice: # You can structure if statements to check if a value is inside a variable or a set (list, dictionary, tuple) etc...
        how_much = int(choice)
        print (how_much)
        print (choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy! You win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print ("There is a bear in here.")
    print ("The bera has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move to the bear.")
    bear_moved = False

    while True:
        choice = input ("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
            
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chew your leg off."
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

        


gold_room()'''
