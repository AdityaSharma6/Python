# **********************************************************
# Assignment: Project 5: Palindrome
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/09)
# Date Completed: (2018/08/09)
#
# Completion time: 1:20 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print("Enter a palindrome of any size: ", end = ' ')
palindrome = input()

list1 = []
list1.extend(palindrome)
list1_length = len(list1)
times = list1_length % 2


if times == 0:
    odd_or_even = "Even"
else:
    odd_or_even = "Odd"
print (odd_or_even)

beginning_index = 0
ending_index = list1_length - 1
beginning_increment = 0
ending_increment = 0

if list1[beginning_index + beginning_increment] != list1[ending_index - ending_increment]:
            print (f"The inputted number: {palindrome} is not a palindrome")
else:
    if odd_or_even == "Even":
        max_counter = list1_length / 2
        counter = 1

        while list1[beginning_index + beginning_increment] == list1[ending_index - ending_increment]:


            beginning_increment += 1
            ending_increment += 1
            counter += 1

            if list1[beginning_index + beginning_increment] != list1[ending_index - ending_increment]:
                print (f"The inputted number: {palindrome} is not a palindrome")
                print ("Clear Even")
        
            if counter > max_counter:
                print ("The inputted number is a palindrome")
                break
    else:
        max_counter = (list1_length +1) / 2
        counter = 1

        while list1[beginning_index + beginning_increment] == list1[ending_index - ending_increment]:

            beginning_increment += 1
            ending_increment += 1
            counter += 1

            if list1[beginning_index + beginning_increment] != list1[ending_index - ending_increment]:
                print (f"The inputted number: {palindrome} is not a palindrome")
                print ("Clear Odd")
        
            if counter > max_counter:
                print ("The inputted number is a palindrome")
                break



   



