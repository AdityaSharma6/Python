from gpiozero import DistanceSensor #imports ultrasonic class
from gpiozero import LED #imports LED class
from gpiozero import PololuDRV8835Robot #imports robot module
import time #imports time module
"""
Authors:
Liam Ward & Aditya Sharma
"""

'''
usonic = DistanceSensor(trigger=16, echo= 13)
distance = usonic.distance # This command recieves the distance

'''
#for personal reference ^

def milestone_one():
    red_led = LED(10)
    green_led = LED(21)

    ultrasonic = DistanceSensor(19, 16)
    
    while True: #changes green or red LED object status based on measured distance
        distance = ultrasonic.distance
        print(distance*100) #to display units in centimeters
        if distance > 0.25:
            green_led.on()
            red_led.off()
        elif distance <= 0.25 and distance > 0.15:
            green_led.off()
            red_led.on()
        elif distance <= 0.15: #allows for 'blinking' of red LED
            red_led.on()
            time.sleep(1) 
            print(distance*100) #Gets it in meters
            red_led.off()
            print(distance*100)
            time.sleep(1)
            
    time.sleep(0.1)
    
def milestone_two(fwd_time, bkwd_time): #moves robot motors forwards or backwards
    robot = PololuDRV8835Robot()
    robot.forward(1)
    time.sleep(fwd_time)
    robot.backward(1)
    time.sleep(bkwd_time)
    robot.stop()
    
def milestone_three():
    robot = PololuDRV8835Robot()
    ultrasonic = DistanceSensor(19, 16)
    while True: #command robot based on distance measurement from ultrasonic sensor
        distance = ultrasonic.distance
        if distance > 0.3:
            robot.forward(0.8) #runs motors forward
        elif distance <= 0.3: #runs robot left for a certain amount of time
            robot.left(0.8)
            user_input = float(input("Enter an amoumt of time: "))
            time.sleep(user_input) #allows for user determination of left turning time
            robot.forward(0.8)
    
def main():
    user_choice_p = int(input("Enter '1' for milestone_one. '2' for milestone two, and '3' for milestone 3: ")) #milestone choice
    if user_choice_p == 1:
        milestone_one()
    elif user_choice_p == 2:
        user_fwd_time = float(input("Enter how long to move the robot forward, in seconds: ")) #forward parameter for milestone two
        user_bkwd_time = float(input("Enter how long to move the robot backward, in seconds: ")) #backward parameter for milestone two
        robot_helper.run(milestone_two(user_fwd_time, user_bkwd_time)) #runs milestone two through the robot
    elif user_choice_p == 3:
        milestone_three()
    else:
        print("You have entered an invalid statement") #accounts for user error in inputs
        main()
    
while True:
    main()

'''
Reflection Questions:

Q1. We could add additional if statements for each different value for the variable
distance. In the if statement, we would say led.on() then time.sleep(1s) then led.off().
We would continue doing this for each different if statement.

Q2. We are not required to initialize pin positions because the robot is not plugged into the bread
board. The robot runs straight through the pi computer, and has its own 'run' command that allows
the code we wrote to be read and run by the robot

Q3. In the speed command: robot.forward() for example, I would put '0.5' instead, as the default
(and maximum) speed is set to 1.0

Q4. I think the motors needed to be slower because at one point they are required to switch directions
almost simultaneously, which puts additional strain on the motors and axis of rotation. If they went
slower, the direction switch may be smoother, but the robot would not travel as fast.

Q5. The robot may not be entirely accurate because there is processing time involved between
the distance measurement, relaying that information back to the computer, then outputting
a command to the motors. This could be tested by quickly crossing the 'distance border' that
we defined as 0.3 meters.

Q6. I would add an 'and' condition into my if statement that involves the >= 30 statement, and thus
set a range between 30 and 80 centimeters where the robot will be turning left.
'''
    
        
    
