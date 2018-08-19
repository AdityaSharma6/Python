# **********************************************************
# Assignment: Boolean Practice
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

print (True and True)       # True
print (False and True)      # False
print (1==1 and 2 ==1)      # False
print ("test" == "test")    # True
print (1 == 1 or 2 != 1)    # True
print (True and 1 == 1)     # True
print (False and 0 != 0)    # False
print (True or 1 == 1)      # True
print ("test" == "testing") # False
print (1 != 0 and 2 == 1)   # False
print ("test" != "testing") # True
print ("test" == 1)         # False
print ( not (True and False)) # True
print ( not (1 == 1 and 0 != 1)) # False
print ( not ( 10 == 1 or 10000 == 10000)) # True
print ( not ("testing" == "testing" and "Zed" == "Cool Guy")) # False
print (1 == 1 and ( not ( "testing" == 1 or 1 == 0))) # True
print ("chunky" == "bacon" and (not ( 3 == 4 or 3 == 3 ))) # False

