# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:48:07 2020

@author: MPH
"""

import datetime as dt
import pandas as pd


done= False
tasks_info={}

#This captures the start date and time automatically from the user's system and asks user to manually input end date and time
client_name = input('Enter client name: ')
task_title = input('Enter task name: ')

import datetime

start2 = ' '
if start2.lower()== 'start':
    start_date = datetime.datetime.now()
else:
    start2 = input('Please enter "start" to capture the start date and time from the system: ')
end_date = input('Enter task end date and time; yy-mm-dd hh-mm-ss: ')
format = '%Y-%m-%d %H:%M:%S'
begin_time = datetime.datetime.now()
end_time = datetime.datetime.strptime(end_date, format)
working_time = (end_time - begin_time)
working_hours = round(float(working_time.total_seconds()/60**2), 2)
money_per_hour = 5
money_earned = round(money_per_hour * working_hours,2)

print('Great job, you worked for ' + str(working_hours) + ' hours and have earned $' + str(money_earned) )





print("Hello, Welcome to Nana's Timesheet"
      "\nTo start type the task number eg. Task 1 for Task 1 or type done to exit."
      "\n\nUse the 24 hour format for the start time and stop time."
      "\nEg. Enter 11:00 for a task starting at 11am and 13:30 for a task ending at 1:30 pm.\n")

while not done:
    #Get task_number
    task_number= input("Enter the name of the task or type done to exit: \n")

    if task_number.lower()!="done":
        tasks_info["Task "+task_number]={}
        #Get Start_time
        begin=input("What time did you start Task "+ task_number+ "? \n")
        tasks_info["Task "+task_number]['Start_time']=begin

        #Get Stop_time
        end=input("What time did you end Task "+ task_number+ "? \n")
        if begin>end:
            end=input("Enter a time after "+begin + "GMT. \nWhat time did you end Task "+ task_number+ "? \n")
        else:
            tasks_info["Task "+task_number]['Stop_time']= end

        #Get duration
        start_dt = dt.datetime.strptime(begin, '%H:%M')
        end_dt = dt.datetime.strptime(end, '%H:%M')
        duration=end_dt - start_dt
        difference=duration.seconds/3600


        #Hourly_rate=float(input("How much did you earn per hour? Enter an integer or a decimal value: \n\n"))
        
        tasks_info["Task "+task_number]['Duration of Work (Hours)']=difference
        tasks_info["Task "+task_number]['Money_earned (Dollars)']=round(float(5*difference))
        

    else: #end loop if done
        #del tasks_info["Taskdone"]
        #tasks_info

        tasks=pd.DataFrame.from_dict(tasks_info)
        Timesheet=tasks.T#transpose dataframe
        
        print("Since Nana earns 5 dollars an hour. Here is his Timesheet.\n")
        print(Timesheet)
        Timesheet.to_excel("Azubi_Python_output"+str(len(Timesheet))+".xlsx", engine="xlsxwriter")
        print("\nThat is it, check on your computer for a document called \nAzubi_Python_output"+str(len(Timesheet))+".xlsx" 
              "\nfor your Timetable in a Microsoft Excel file")
       
        done=True
            
