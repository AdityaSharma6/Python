# Understanding Functions in Python

def addition ():
    print ("The function you have called is known as the \"addition\" function")
    print ("Initializing \"addition\" function")
    number1 = float (input ("Enter the first number: "))
    number2 = float (input ("Enter the second number: "))
    sum = number1 + number2
    print (f"{number1} + {number2} = {sum}")
    print ("Function processing complete. \n")
    return sum # This stores a value into the function name. When the functino name is called upon again, the value that is "returned" is utililized. In this case of the program, the value that is returned is eventually printed.
addition_output = addition() # You cannot equate "addition_ouput" to "sum" because you cannot call a variable that was used within a function

def literacy ():
    print ("Dear User, please tell us who you consider to be your king?")
    king = input ()
    return king # If you write another return statement again, the system will simply skip it.
literacy_output = literacy()

def return_statement_test():
    print ("Here, I will display another function of the return statemnet")
    print ("How many gods exist?")
    return "idk"
return_output = return_statement_test()

print ("\nThe functions have been run. The results will now be displayed.")
print (addition_output)
print (literacy_output)
print (return_output)

sum = float(input("One Number: ")) + float(input("Enter 2nd number: "))
# When needing to find the sum of two numbers, you can write it like this to make it short.

print (sum) # Whenever you want to call the value of a variable and display it, it needs to be within brackets


