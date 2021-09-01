import mysql.connector as sql
from time import sleep 
db = sql.connect(host = "localhost",user = "root",password="password123",database ="dharul")
cur = db.cursor()
run = "y"

while run == "y":
    what_main = input("\nPress 1 to enter data\nPress 2 to read existing data\nPress 3 to search for data\nPress 4 to delete existing data\nPress 5 to exit\n")
    
    if what_main == "1":
            adno = int(input("Enter Admission NO  :  "))
            naam = input("Enter Name :  ")
            kaksha = input("Enter Class  :  ")
            roll = int(input("Enter Roll NO  :  "))
            cur.execute(f"""insert into school
            values({adno},"{naam}","{kaksha}",{roll})
            """)
            db.commit()            
            task = input("Do you want to continue adding data? <y/n>  :  ")

    elif what_main == "2":
        cur.execute("select * from school")
        a = cur.fetchall()
        l = []
        for i in a:
            l.append(f"Admission No : {i[0]}")                          
            l.append(f"Name : {i[1]}")
            l.append(f"class : {i[2]}")
            l.append(f"Roll No : {i[3]}")
            print(l)
            l = []

    elif what_main == "3":
            bases_of_search = input("\nPlease enter the searh keyword\n") 
            cur.execute(f"""select * from school
            where Adm_no like {bases_of_search} or name like '{bases_of_search}' or class like '{bases_of_search}' or roll_no like {bases_of_search}""")
            a = cur.fetchall()
            if len(a) == 0:
                print("No record found")
            else:
                l = []
                for i in a:
                    l.append(f"Admission No : {i[0]}")                          
                    l.append(f"Name : {i[1]}")
                    l.append(f"class : {i[2]}")
                    l.append(f"Roll No : {i[3]}")
                    print(l)
                    l = []
                     
    elif what_main == "4":
            bases_of_del = input("\nPlz enter the word whoose data you want to delete\n")
            cur.execute(f"""select * from school
            where Adm_no like {bases_of_del} or name like '{bases_of_del}' or class like '{bases_of_del}' or roll_no like {bases_of_del}""")
            a = cur.fetchall()
            if len(a) == 0:
                print("No record found") 
            elif len(a) >= 1:   
                cur.execute(f"""DELETE from school
                where Adm_no like {bases_of_del} or name like '{bases_of_del}' or class like '{bases_of_del}' or roll_no like {bases_of_del}""")
                db.commit()
                print("Data deleted successfully")
    elif what_main == "5":
        run = "Bye"
    
    else:
        print("\t\tWrong Input !!! try again")
    
print("Thx for using a small Programe\n\t\t\t-By DHARUL")
sleep(3)