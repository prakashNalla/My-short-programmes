def getdate():
    import datetime 
    return datetime.datetime.now()

name = input("Enter your name\n")
name = name.lower()
run = "y"

# '''
def log_d(a):
    filename = name+"_study_time.txt"
    f = open(filename,"a+")      
    f.write(f"[{getdate()}]\t: {a}\n")
    f.close()

def log_e(a):
    filename = name+"_wastage.txt"
    f = open(filename,"a+") 
    f.write(f"[{getdate()}]\t: {a}\n")
    f.close()

def retrieve_d():
    filename = name+"_study_time.txt"
    f = open(filename,"r") 
    ret= f.read()
    return ret 

def retrieve_e():
    filename = name+"_wastage.txt"
    f = open(filename,"r") 
    ret= f.read()
    return ret

try:
    while(run == "y"):
        what1 = input("What you want to access\n1 for study_time 2 for wastage\n")
        what2 = input("What you want to do \n1 for log or 2 for retrieve\n")
        if what1 == "1":
            if what2 == "1":
                a = input("What you Study and how much?\n") 
                a = a + "  Hours"
                log_d(a)
            elif what2 == "2":
                print(retrieve_d())
        
        elif what1=="2":
            if what2 == "1":
                a = input("What you did and For how long?\n")
                a = a + "  Hours" 
                log_e(a)
            elif what2 == "2":
                print(retrieve_e())
        else : 
            print("!!! Wrong Input !!!")
        run = input("do you want to continue??\nPress y to continue and n to exit\n")
        run = run.lower()
except Exception as e:
    print(e)
# '''
