user_time = input("Enter the time in this format: hh:mm:ss. \n Enter: ")

list1 = user_time.split(":")

hours = int(list1[0])
minute = int(list1[1])
seconds = int(list1[2])

total_seconds_elapsed = (hours*3600) + (minute*60) + seconds
print (total_seconds_elapsed)
