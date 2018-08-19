# **********************************************************
# Assignment: Making Decisions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/06)
# Date Completed: (2018/08/06)
#
# Completion time: 20 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("""You enter a dark room with two doors.
You have no choice but to enter a room.
Which door do you enter?
Door 1 or Door 2? """)

door = float(input(" > "))
print ("\n")

if door == 1:
    print ("There is a giant bear here eating a cheese cake.")
    print ("What do you do?")
    print ("""Here are your options: 
    Option 1: Take the cake.
    Option 2: Scream at the bear. """)

    bear = float(input(" > "))

    if bear == 1:
        print ("The bear eats your face off. Good Job!")
    elif bear == 2:
        print ("The bear only eats your legs off. Good job!")
    elif bear > 2:
        print("I said you can only select Option 1 or Option 2.")
    else:
        print (f"Well, doing {bear} is probably better.")
        print ("Bear runs away.")

elif door == 2:
    print ("You stare into the endless abyss at Cthulhu's retina.")
    print (" 1. Blueberries.")
    print (" 2. Yellow Jacket Clothespins.")
    print (" 3. Understanding revolvers yelling melodies.")

    insanity = float(input("> "))

    if insanity == 1 or insanity == 2:
        print ("Your body survivers powered by a mind of jello.")
        print ("Good Job")
    else:
        print ("The insanity rots your eyes into a pool of muck.")
        print ("Good JOb")

else:
    print ("You stumble around and fall on a knife and die. Good Job!")



