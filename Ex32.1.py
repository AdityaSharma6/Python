# **********************************************************
# Assignment: Loops and Lists Part 1
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/06)
# Date Completed: (2018/08/07)
#
# Completion time: 5 hours 
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

# To add an item to the list use .append(). This adds another entry to the end of the list
# To remove an item from the list use .remove(). You can only remove one item from the list per command. You mention what you want to remove from the list within the brackets of the command.
# To find the length of the list use .len(). This mentions the amount of values that the machine reads (1 less than humans)

list1 = [ 1, 2, 3, 4, 5, 6 ]
list2 = [ "Aditya", "Poonam", "Noor", "Tulsi", "Archana", "Yuvraj", "Pooja" ] # When storing text, use quotations. The type of quotations does not matter: " vs '

print (list1) 
print ("\n")

# The first item in a list to a human has the number 1. However, to a system, it has the number 0
# The items within a list can be changed by identifying the list and the number that is associated with the value you'd like to change
list1 [0] = "Aditya"
list1 [1] = "Is"
list1 [2] = "Going"
list1 [3] = "To"
list1 [4] = "University"
list1 [5] = input ("When are you going to university: Say \"On\" as your response. ")
print ("\n")

print (list1)
print ("The length of this list to a human is",len(list1), "values long. But, the length of the list to the machine is", len(list1) - 1,".") # The function len() retrives an integer data type. You cannot concatenate with the addition symbol; thus, you must use the comma. The comma lets you concatenate values that are different data types.
print ("\n")

print ("Would you like to increase the size of your list?", end = ' ')
response1 = input()
print ("\n")

if response1 == "Yes" or response1 == "yes":
    list1 .append(input("Enter another value: "))
    print (list1)
    print ("The length of this list to a human is now", len(list1), "values long. But, the length of the list to the machine is", len(list1) - 1, ".")
    print ("The final word you added was", list1 [6])
    print ("\n" * 10)
else:
    print ("This is the end of the program.")

print (list1)
list1 .remove("Going")
print (list1)


list3 = ["ford", "mistsubishi", "Bmw", "ferarri"]
list4 = [1, 2, 3, 4, 5]
# list3.append(11)  # Adds mentioned element to the end of the list
# list3.clear()     # Empties list
# list3.copy()      # Copies list & its elements
# list3.count()     # Counts the number of times a specific element shows up in a list
# list3.extend()    # The input needs to be a variable holding strings or a string itself. It breaks the string into its characters and adds it to the end of the list specified.
# list3.index()     # Takes a input and searches the list for the first equavalent inputted value first value. Then, it will output the slot number within which the input resides in. 
# list3. insert()   # Replaces the element at the specified position 
# list3.pop()       # Removes the element at the specified location
# list3.remove()    # Removes the first item with the specified value
# list3.reverse()   # Reverses the order of the list
# list3.sort()      # Sorts the list in an ascending fashion #list3.sort(reverse=true) sorts in descening

