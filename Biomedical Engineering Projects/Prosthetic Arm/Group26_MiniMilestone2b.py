import math
import time

def gear_ratio (level1, level2): #Accepts lists as arguements. Lists correspond to series of Pitch Diameters
    #12, 18 - Idler, 36
    #12, 13, 13, 20
    # Thumb: 20, 20
    gear_ratio1 = level1[2] / level1[0]
    gear_ratio2 = level2[3] / level2[0]
    total_gear_ratio = gear_ratio1 * gear_ratio2
    return total_gear_ratio

def number_motor_rotations(forefinger_rotation, total_gear_ratio): #FF Rot is in degrees
    total_motor_rotation = total_gear_ratio * forefinger_rotation/360
    return total_motor_rotation

def finger_position(forefinger_length, angular_position): #AP is in degrees. Tip to base angle
    angular_position_radians = angular_position * (math.pi/180)
    x = round(math.cos(angular_position_radians) * forefinger_length, 2)
    y = round(math.sin(angular_position_radians) * forefinger_length, 2)
    coordinate = [x,y]
    #print(coordinate)
    return coordinate

def elapsed_time (input_speed, number_motor_rotations):
    elapsed_time = round(((number_motor_rotations / input_speed) * 60),2)
    return elapsed_time

def main():
    input_speed = 45
    level1 = [12,18,36]
    level2 = [12,13,13,20]
    forefinger_length = 0.41
    time_elapsed = elapsed_time(input_speed, number_motor_rotations (90, gear_ratio(level1, level2)))
    
    angular_position = 0
    for i in range (10):
        print(finger_position(forefinger_length, angular_position)[0], "\t", finger_position(forefinger_length, angular_position)[1], "\t", "forefinger position at ",angular_position, "degrees rotation")
        angular_position += 10 # Starts at 0 --> FF Rotation. Open = 0, closed = FF Rotation

    print("\nSTATUS \t ELAPSED TIME")
    for i in range (6):
        if (i%2 == 0):
            print("OPEN \t", time_elapsed * i)
        else:
            print("CLOSED \t", time_elapsed * i)
    print("OPEN \t", time_elapsed * (i+1))


main()
'''
import math
def number_motor_rotation(Forefinger_rot,total_gear_ratio):
    number_of_motor_rotations = (total_gear ratio)*((forefinger_rot)/360)
    return number_of_motor_rotations

def finger_position(length_forefinger,Angular position):
    Angular_position_radians=(Angular_position)*(3.14/180)
    x = math.cos(Angular_position_radians)*(length_forefinger)
    y = math.sin(Angular_position_radians)*(length_forefinger)
    

def elapsed_time(input_speed,Number_of_motor_rotations):
    elapsed_time = (Number_of_motor_rotations/60)/(input_speed)
    return elapsed_time
'''