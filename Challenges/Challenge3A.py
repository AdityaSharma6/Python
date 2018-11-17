# **********************************************************
# Assignment: Challenge 2
#
# Description: Question:
# With a given integral number n, write a program to generate
# a dictionary that contains (i, i*i) such that is an integral 
# number between 1 and n (both included). and then the program 
# should print the dictionary. Suppose the following input is 
# supplied to the program: 8 Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Author: Aditya Sharma
#
# Date Start: (2018/11/17)
#
# Completion time: 2 minutes
#
# Honor Code: I pledge that this program represents my own
# program code. I received help from (enter the names of
# others that helped with the assignment; write no one if
# you received no help) in designing and debugging my program.
# *********************************************************
'''
number = 8
dictionary1= {}
# Dictionaries use curly brackets. Lists use square brackets and tuples uses god knows what lmao
# Dictionaries are initialized the way lists are usually initialized but can also be initialized this way

for i in range (0, (number+1)): # The range function says "In the range of "first value" to "last value -1". It always stops 1 value less than the mentioned final value
    dictionary1 [i] = i*i
    # Dictionaries have a specific syntax. They have keys and values
    # The key needs to be specified so that it can store a specific value
    # Values can be added by mentioning the key and the respective value
    # Keys can be set to store numerical and alphabetical values. To store alphabetical values, simply include the quotation marks

print(dictionary1)
'''

squares = int(input("How many squares would you like to see? "))
dictionary1 = {}

for i in range (0, (squares+1)):
    dictionary1 [i] = i*i

print (dictionary1)


