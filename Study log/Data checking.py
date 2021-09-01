def getdate():
    import datetime 
    return datetime.datetime.now()

name = input("Enter your name\n")
name = name.lower()
run = "y"
# '''
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
        sub = input("Type the word u want to search with\n")
        filename = name+"_study_time.txt"
        f = open(filename,"r")   
        len = len(f.readlines())
        f.close
        if what1 == "1":
            filename = name+"_study_time.txt"
            f2 = open(filename,"r")   
            for i in range(0,len):
                sub_C = f2.readline()          
                if sub in sub_C :
                    print(sub_C)

        elif what1=="2":
            filename = name+"_study_time.txt"
            f2 = open(filename,"r")   
            for i in range(0,len):
                sub_C = f2.readline()          
                if sub in sub_C :
                    print(sub_C)
        else : 
            print("!!! Wrong Input !!!")
        run = input("do you want to continue??\nPress y to continue and n to exit\n")
        run = run.lower()
except Exception as e:
    print(e)