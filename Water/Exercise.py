from pygame import mixer
mixer.init()
from time import time , sleep
from datetime import datetime
run = "y"
start_time = time()
samay = eval(input("\nTime after which u want 2 Move\n"))
samay = samay*60
print("\t\tWELCOME")
while run =="y":
    a = "-_-"
    sleep(samay)
    curtime = time()
    diff = curtime - start_time
    if diff > samay:
        mixer.music.load("Thunder.mp3")
        mixer.music.play(-1)
        while a !="y" and a !="re" and  a != "change" and a != "reset" and a!="exit":
            a = input(f"Have u done - [{datetime.now()}]\n")
            a = a.lower()
            if a == "y":
                start_time = time()
                mixer.music.pause()
                print(f"Done at : {datetime.now()}\n")
            elif a=="re" or a == "change" or a == "reset":
                start_time = time()
                mixer.music.pause()
                samay = eval(input("\nTime after which u want 2 Move\n"))
                samay = samay*60    
            elif a=="exit":
                run == "n"
            elif a == "n" :
                print("\nTho hill le na bsdk\n")
                continue
            else:
                continue 
        
                        
            
    

