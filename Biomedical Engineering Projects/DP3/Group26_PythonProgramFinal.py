from time import sleep
from pcf8591 import PCF8591
import math
from gpiozero import PWMOutputDevice
# Above, all the libraries and modules that will be required have been imported.
# Below, all the variables that I will require have been defined. It is imperative that the significance of these variables are understood.
adc = PCF8591()
sensor1 = []
sensor2 = []
sensor3 = []
sensor4 = []
sensor_list = [sensor1, sensor2, sensor3, sensor4]
sensor_averages = []
highest_input_sensor = 0
motor1 = PWMOutputDevice(12,True)
motor2 = PWMOutputDevice(16,True)
motor3 = PWMOutputDevice(20,True)
motor4 = PWMOutputDevice(21,True)
motor_list = [motor1, motor2, motor3, motor4]
motor1.value = 0
motor2.value = 0
motor3.value = 0
motor4.value = 0
bodyweight = 150                            # Since our device is custom made, depending on the weight of the user, this value can be altered.
bodyweight_range = 0.1*bodyweight
approx_equal_values = []


def sensor_calibration():
    '''
    This function's purpose is to calibrate the sensors. This is because we noticed that when the sensors were not experiencing any force,
    they still returned non-zero values. We also noticed that each time they turned on, they would return a different base value than before.
    Thus, we needed to calibrate them and bring them down to zero. This is what the current function accomplishes.
    '''
    offsets = [0,0,0,0]                                     # Sets initial values to be 0. Each (index + 1) in the list corresponds to the sensor number. Ex: Index 0 corresponds to sensor 1. Index 1 corresponds to sensor 2. Etc...
    sleep(0.5)
    for i in range(4):                                      # Collects the base value of the sensors 
        offsets[i] = -adc.get_channel(i)
        sleep (0.5)                                         # Flips the sign of the initial value so that when it is stored, it can be added to the initial value to bring it to 0
    return offsets



def value_retrieval(list1, list2, list3, list4):
    '''
    The purpose of this function is to retrieve the individual values of each sensor and store it in the sensor's own unique list. 
    '''
    offsets = sensor_calibration()
    counter = 0
    while counter < 30:
        sensor1.append(abs(adc.get_channel(0) + offsets[0])) # Acquires data from sensor (input). Then, it is added to its offset and the sum is stored in a list
        sensor2.append(abs(adc.get_channel(1) + offsets[1])) 
        sensor3.append(abs(adc.get_channel(2) + offsets[2]))
        sensor4.append(abs(adc.get_channel(3) + offsets[3]))
        sleep(0.1)
        counter += 1


def calculation():
    list_sum = 0
    for i in range(len(sensor_list)):                       # This enters a list which contains another list and iterates through it. 
        '''
        Since the variable sensor_list stores all the lists within it in seperate indexes. If I want to find the average of each individual list, I need to somehow
        access this multidimensional array. I can do this by using 2 loops. The first loop will enter the indexes of the initial list. The second loop (below) will
        enter the actual values of the list.
        '''
        for j in sensor_list[i]:
            list_sum = j + list_sum                         # Finds sum
        list_average = list_sum / len(sensor_list[i])
        sensor_averages.append(list_average)                # Finds average
        list_sum = 0
                             

def decision():
    '''
    The purpose of this function is to determine which sensor is experiencing the maximum force. This function also considers the test cases. The logic behind
    the test cases will be explained further below. Currently, we have found the average of each of the values that each sensor experiences and have them stored
    in a list. This list has a length of 4 and each index corresponds to that respective sensor's average value. 
    Ex: [10,11,12,13] This means that at index 0, Sensor 1 has an average value of 11. At index 1, Sensor 2 has an average value of 11 etc...
    We will use this to determine the largest values within the list provided that they are within a range of +/- 10% of the bodyweight of the largest value.  
    '''
    global highest_input_sensor
    greatest_value = -100
    counter = 0
    
    for i in range(3):                                      # This determines which value within the list has the greatest value.
        if sensor_averages[i] > greatest_value:
            greatest_value = sensor_averages[i]

    for j in range(3):                                      # Determines which sensor has the highest reading
        if sensor_averages[j] == greatest_value:
            counter = j+1

    for k in range(3):                                      # This determines if any other values within the list fall within the specified range.
        if sensor_averages[k] > (greatest_value - bodyweight_range):        # The range is +/- 10% of the overall bodyweight in relation to the greatest value. 
            '''
            This determines if there are 1+ values that are within the range of the bodyweight. If there is only 1 greatest value, then the value will have been stored
            within the list because it falls within the range definition. However, if there are multiple items, then their indexes are also stored to the list.
            '''
            approx_equal_values.append(k+1)

    if len(approx_equal_values) > 1: 
        highest_input_sensor = approx_equal_values
    else:
        highest_input_sensor = approx_equal_values


def output():
    ''' 
    The purpose of this function is to analyze the data and determine which output is appropriate. Since our device incorporates vibration motors that will
    vibrate at the location on the sole that experiences the largest force. This function will essentially tell the motors to vibrate at the locations that
    experience the largest force.
    '''
    global highest_input_sensor
    for i in highest_input_sensor: 
        '''
        Since the highest_input_sensor list stores the index values of the sensors that are experiencing the most force. This loop will be used to
        turn on all the motors that correspond to their sensors. This is also the test case.

        This acts as the test case as well because depending on how many sensors are deemed to have the largest values, the same number of motors will vibrate.
        Our test cases are the following:
        ) There is only 1 max value. In which case, only 1 motors will vibrate
        2) There are 2 max values. In which case, 2 motors will vibrate
        3) There are 3 max values. In which case, 3 motors will vibrate

        This loop allows for the successful testing of the test cases.
        '''
        motor_list[i-1].value = 1
        
    sleep(15)                                   # The motors will vibrate for 15 seconds
    
    for i in highest_input_sensor:              # This loop turns off the motors after they are done vibrating.
        motor_list[i-1].value = 0


def main():                                     # This is the main function. It calls all the other functions.
    value_retrieval(sensor1, sensor2, sensor3, sensor4)
    calculation()
    decision()
    output()

main()












