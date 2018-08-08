# **********************************************************
# Assignment: Exercise 25: Even More Practice
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/05)
# Date Completed: (2018/08/05)
#
# Completion time: 120 minutes
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

def break_words(stuff): # Function breaks up the word into pieces
    words = stuff.split(' ')
    return words
    
def sort_words (words): # Function sorts the words alphabetically
    return sorted(words)

def print_first_word(words): # Function prints first word after seperating it from entire string
    word = word = words.pop(0)
    print(word)

def print_last_word(words): # Function prints last word after seperating it from the entire string
    word = word.pop(-1)

def sort_sentence(sentence): # Registers the entire sentence and sorts all the words
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence): # Prints the first and last words of the string
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


