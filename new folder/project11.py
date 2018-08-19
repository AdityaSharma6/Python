# **********************************************************
# Assignment: Project 11: Check Primality Functions
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/17)
# Date Completed: (2018/08/17)
#
# Completion time: 3:20 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************
'''
number = int(input("Input a number: "))

divisor = 2
prime = 0



while divisor < number:
    if (number % divisor) == 0:
        print (f"{number} is wholly divisible by {divisor}. Therefore, {number} is not a prime number.")
        prime = prime + 1
        break
    divisor = divisor + 1

if prime == 0:
    print (f"{number} is a prime number because it has 0 divisors.") '''

def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer()

if age > 15:
    print("You are over the age of 15")
    print("You are in grade " + str(school_year))





'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.

Discussion

Concepts for this week:

Functions
Reusable functions
Default argument
'''