"""
Write a program to set a simple alarm clock with a specified time.
1) take input for time in following format (HH:MM)
2) 


"""
import datetime
import time

z = datetime.datetime.now() 
y = z.strftime("%d-%m-%Y %I:%M:%S")

 
while True:
    # Get user input for alarm time
    z = input("enter time to set alarm in following format. (HH:MM)") 
    alarm_time = []
    split_input = z.split(":")
    for i in split_input:
        alarm_time.append(int(i))

# Validate the time entered to be between 0 and 24 (hours) or 0 and 60 (minutes)
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False


