# **********************************************************
# Assignment: Exercise 17: Reading and Writing Files
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/07/31)
# Date Completed: (2018/07/31)
#
# Completion time: 120 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

from sys import argv
from os.path import exists

script, from_file_1, to_file_2 = argv # ex17_file1 and ex17_file2

print ("Exercise 17: Transfer contents from file1 to file 2 and vice versa." + "\n")
print (f"Initiating copy from {from_file_1} to {to_file_2}" + "\n")

open_from_file_1 = open (from_file_1) # Opened the file
data_from_file_1 = open_from_file_1.read() # Stored the contents


open_to_file_2 = open (to_file_2).read() # Opened the other file
data_to_file_2 = open_to_file_2.read() # Stored ITS contents


# The next 2 lines prints the contents of both files.
print (f"This is the contents of file1: {data_from_file_1}" + "\n")
print (f"This is the contents of file2: {data_to_file_2}" + "\n")

open_from_file_1 = open (from_file_1, 'w') # This needs to be done if the file will be cleansed.
open_to_file_2 = open (to_file_2, 'w')

open_from_file_1.truncate()
open_to_file_2.truncate()

open_from_file_1.write(data_to_file_2)
open_to_file_2.write(data_from_file_1)

print ("\n" + "Transfer complete.")

open_from_file_1.close()
open_to_file_2.close()

# You can chain stuff... "open(file1).read()"



# open()
# truncate()
# readline






