from pygame import mixer
mixer.init()
from time import time , sleep
from time import strftime
from datetime import datetime

print("\n\t\tWELCOME")

run = "y"
start_time = time()
samay = eval(input("\nTime after which u want 2 drink\n"))
samay = samay*60
no_alert_time_req = input("Is there any time when u dont want alerts    (y/n)\n")

if no_alert_time_req == "y":
    class_time_start = input("\nThe time at which u dont want to drink - (in 24 h format [hh:mm])\nEnter the starting time     -   ")
    class_time_end = input("Ending time     -   ")
    class_time_start_lst = class_time_start.split(":")
    class_time_end_lst = class_time_end.split(":")
    print()
else: 
    pass

while run =="y":
    a = "-_-"
    sleep(samay)
    curtime = time()
    diff = curtime - start_time
    
    if diff > samay:
        if no_alert_time_req == "y":
            class_check = strftime("%H:%M:%S")
            class_check_lst = class_check.split(":")
            if class_check_lst > class_time_start_lst and class_check_lst < class_time_end_lst :
                sleep_time = (((int(class_time_end_lst[0]) - int(class_time_start_lst[0]))*60) + (int(class_time_end_lst[1]) - int(class_time_start_lst[1])))*60 + 1
                print("\n\t\tAlerts paused")
                sleep(sleep_time)
        if no_alert_time_req != "y":
            pass
        mixer.music.load("paani.mp3")
        mixer.music.play(-1)
                
        while a!="y" and a!="re" and  a!="change" and a!="reset" and a!="exit" and a!="class" and a!="no alert" and a!="mute" and a!="ct":
            a = input(f"Have u drinken water - [{datetime.now()}]\n")
            a = a.lower()
                        
            if a == "y":
                start_time = time()
                mixer.music.pause()
                        
            elif a=="re" or a == "change" or a == "reset":
                start_time = time()
                mixer.music.pause()
                samay = eval(input("\nTime after which u want 2 drink\n"))
                samay = samay*60    
                        
            elif a=="class" or a == "no alert" or a == "mute" or a == "ct":
                start_time = time()
                mixer.music.pause()
                no_alert_time_req = "y"
                class_time_start = input("\nThe time at which u dont want to drink - (in 24 h format [hh:mm])\nEnter the starting time     -   ")
                class_time_end = input("Ending time     -   ")
                class_time_start_lst = class_time_start.split(":")
                class_time_end_lst = class_time_end.split(":")
                        
            elif a=="exit":
                run == "n"
                        
            elif a == "n" :
                print("\nTho pee na bsdk\n")
                continue
                        
            else:
                continue

                        
            
    

