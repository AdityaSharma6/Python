"""
Authors:
Liam Ward 400170514
Aditya Sharma 400189221
Emily Kim 400213481


"""
def milestone_one():
    while True:
        user_input = input("Enter ON or OFF or Q: ")
        user_input = user_input.upper()
        if user_input == "ON":
            print("Turning the light on")
        elif user_input == "OFF":
            print("Turning the light off")
        elif user_input == "Q":
            print("Goodbye")
            break
        else:
            print("Invalid Input. Please try again")

def milestone_two():
    from gpiozero import LED #gpiozero only imports from rasberry pi
    from gpiozero import Button
    import time
    light = LED(20)
    push = Button(21)
    light.off()
    boolean_variable = False 
    
    while True:

        if push.is_pressed is True and boolean_variable == False:
            time.sleep(0.3)
            light.on()
            boolean_variable = True
            
        elif push.is_pressed is True and boolean_variable == True:
            time.sleep(0.3)
            light.off()
            boolean_variable = False
            
def milestone_three():
    from gpiozero import PololuDRV8835Robot
    import time
    robot = PololuDRV8835Robot()
    userForwardInput = float(input("How long to move the robot forward, in seconds: "))
    userBackwardInput = float(input("How long to move the robot backward, in seconds: "))
    robot.forward(1)
    time.sleep(userForwardInput)
    robot.backward(1)
    time.sleep(userBackwardInput)
          
        
        
def main():
    milestone_one()
    milestone_two()
    user_input1 = input("Would you like to run Milestone 3? Answer YES or NO: ")
    if user_input1 == "YES":
        milestone_three()
main()
'''
Reflective QUestions:
1. No, it would not run as intended, python is case-sensitive.

1B. We would modify it by using the .upper() method which turns
all the characters in a string to uppercase alphabets

2. We would put 2 other if statements within each if or elif statement to check
if the light was already on or off and respond accordingly(with new print statements)

3. We pause the program for a brief period (0.3S) so that the light does not flicker
constantly between its on and off states and blow out.

4. I would add the light.off() command after a time.sleep(3) 3 second delay in the if
statement that controls whether the light is on or not

5. I would add light.on() in the beginning before the while loop and change the
push variable to push = LED(18)

6. We used a specific robot library so the locations are already specified in the other code

7. To modify the program to run the motors at 50% speed, I would change the "1" value
in the robot.forward() and robot.backward() commands to "0.5" instead

'''
