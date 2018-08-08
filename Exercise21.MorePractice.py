# **********************************************************
# Assignment: Exercise: MORE PRACTICE Functions 
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/04)
# Date Completed: (2018/08/4)
#
# Completion time: 30
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("Let's practice everything.")
print ('You\'d need to nkow \'about escapes with \\ that do:') 

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print(secret_formula(started))