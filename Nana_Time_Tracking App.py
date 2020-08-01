# -*- coding: utf-8 -*-

import datetime as dt
import time
import pandas as pd


done= False
tasks_info={}


print("Hello, Welcome to Nana Timesheet Tracking App"
      "\nThis app allows you to track multiple tasks. \nTo Start,\n")
      
while not done:
    #Get task_title
    task_title= input("Enter the name of the task to record the start time or \nType done to exit the app: \n")
    print(f'Okay, the timer is running for {task_title}')

    if task_title.lower()!="done":
        tasks_info["Task "+task_title]={}
        #Get Start_time
        
        start=str(dt.datetime.now())
        s=time.perf_counter()
        format1 = '%Y-%m-%d %H:%M:%S.%f'
        start_dt = dt.datetime.strptime(start, format1)
        #tasks_info["Task "+task_title]['C (Start_time)']=start_dt
        tasks_info["Task "+task_title]['A (Start_timer)']=s

        #Get Stop_time 
        
        #validating that the user entered the key word stop to record the stop time
        check=False
        
        while not check:
            stop=input("Type stop to halt the timer and record the time you ended:"+ task_title "+ :")
            if stop.lower()=="stop":
                end=str(dt.datetime.now())
                e=time.perf_counter()
                end_dt = dt.datetime.strptime(end, format1)
                #tasks_info["Task "+task_title]['D (Stop_time)']=end_dt
                tasks_info["Task "+task_title]['B (Stop_timer)']=e
        
                #Get duration, how long the person worked
                working_time=end_dt - start_dt
                working_hours=float(working_time.seconds)
                diff=float(e-s)
                hours=diff/3600

                #calculating money earned
                money_per_hour = 5
                money_secs=money_per_hour/3600
                money_earned = float(money_secs * working_hours)
                smoney=float(money_secs*diff)
                money_hours=float(money_per_hour*hours)
                
                
                #tasks_info["Task "+task_title]['E (Duration of Work in Hours)']=working_hours
                tasks_info["Task "+task_title]['F (Duration of Work in Seconds)']=diff
                tasks_info["Task "+task_title]['G (Duration of Work in Hours)']=hours
                #tasks_info["Task "+task_title]['J (Money_earned Dollars)']=money_earned
                tasks_info["Task "+task_title]['H (Money_s_per Dollars)']=smoney
                #tasks_info["Task "+task_title]['I (Money_h_per Dollars)']=money_hours
                                  
                #print(f'\nGreat job, you worked for {working_hours} secss {diff} secs \nand have earned $ {money_earned} or {smoney}')
                print(f'\nGreat job, you worked for  {diff} secs or {hours} hours \nand have earned $  {smoney}\n')
                check=True
        

    else: #end loop if done

        tasks=pd.DataFrame.from_dict(tasks_info)
        Timesheet=tasks.T #transpose dataframe
        
        print("\nSince Nana earns 5 dollars an hour. Here is his Timesheet.\n")
        print(Timesheet)
        Timesheet.to_excel("Azubi_Python_output"+str(len(Timesheet))+".xlsx", engine="xlsxwriter")
        print("\nThat is it, check on your computer for a document called \nAzubi_Python_output"+str(len(Timesheet))+".xlsx" 
              "\nfor your Timesheet in a Microsoft Excel file.")
       
        done=True






