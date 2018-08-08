# **********************************************************
# Assignment: Exercise 16: Reading and Writing Files
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

'''
Function 1: "close" - It saves and closes the file
Function 2: "read" - It reads & stores the contents of the file. You can assign the result to a variable.
Function 3: "readline" - It reads & stores the content pf just one line of a text file. You can store the result to a variable.
Function 4: "truncate" - It empties the file
Function 5: "wrie('stuff') - It writes new stuff into the file
Function 6: "seek(0) - It moves the read/write location to the beginning of the file
'''

from sys import argv 

script, filename = argv  

print (f"We are going to erase {filename}")
print ("If you don't want that, hit CTRL - C (^C)")
print ("If you do want that, hit RETURN.")
print ("Waiting...")

# The following 2 lines utilize user input. 
print (f"What is your response? Would you like to erase {filename}?", end = ' ') # If you turned the "print" to "input", then the user's response would be on the next line. But, by using print and ending with " end = ' ' ", the user's response is on the same line
response = input()

print ("Opening the file...")
target = open (filename, 'w') # Here, a variable is created. The variable's value is the file that is opened. This means that the open file is saved to the variable.

print ("Your response indicates that we erase the file's contents. Goodbye!")
target.truncate() # This is a command which tells the computer to empty the variables contents. Since the open file is saved to the variable, the file's contents are being erased.

print ("We will now re-write the file's contents. You will be prompted 3 times and each time, you will write what you'd like to be written in the file.")
line1 = input ("This is prompt #1.  ")
line2 = input ("This is prompt #2.  ")
line3 = input ("This is prompt #3.  ")

# The following commands tell the system to place the "line#" variable's contents into the open file which is saved in the variable "target"
target.write (line1 + "\n" + line2 + "\n" + line3 + "\n")

print ("Now, at this point we have opened, cleared, edited the file. We are now going to save and close the file.")
target.close() # This tells the computer to close the targetted file.

# Line 41 has a command which opens the file. It also has a command which clears the files contents. This command is given by the ", 'w' " part of the code. When this command is here, the command on line 44 is not needed.
# The truncate command also empties the file but it is unable to further empty the file because the command on line 41 already emptied it.
# This makes it so that you can only have 1 of both commands.