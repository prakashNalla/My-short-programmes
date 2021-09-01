import mysql.connector as sql
from time import sleep 
db = sql.connect(host = "localhost",user = "root",password="password123",database ="dharul")
cur = db.cursor()
run = "y"
task = "y"
while run == "y":
    what_main = input("\nWhat u want 2 do?\nPress 1 to enter data\nPress 2 to read existing data\nPress 3 to search for data\nPress 4 to delete existing data\n")
    
    if what_main == "1":
        while task == "y":
            adno = int(input("Enter Admission NO  :  "))
            naam = input("Enter Name :  ")
            kaksha = input("Enter Class  :  ")
            roll = int(input("Enter Roll NO  :  "))
            cur.execute(f"""insert into school
            values({adno},"{naam}","{kaksha}",{roll})
            """)
            db.commit()            
            task = input("Do u want to continue adding data??\n")

    elif what_main == "2":
        cur.execute("select * from school")
        a = cur.fetchall()
        for i in a:
            print(i) 
        
    elif what_main == "3":
        while task == "y":
            bases_of_search = input("\nhow u want to search\nPress 1 to search using Admission no\nPress 2 to search using name\nPress 3 to search using class\nPress 4 to search using roll no\n") 
            if bases_of_search == "1":
                adno = int(input("Enter Admission NO  :  "))
                cur.execute(f"""select * from school where Adm_no like {adno}""")
                a = cur.fetchall()
                for i in a:
                    print(i)
                
            elif bases_of_search == "2":
                naam = input("Enter Name :  ")
                cur.execute(f"""select * from school where Name like '{naam}'""")
                a = cur.fetchall()
                for i in a:
                    print(i)
                
            elif bases_of_search == "3":
                kaksha = input("Enter Class  :  ")
                cur.execute(f"""select * from school where class like '{kaksha}'""")
                a = cur.fetchall()
                for i in a:
                    print(i)
                
            elif bases_of_search == "4":
                roll = int(input("Enter Roll NO  :  "))                
                cur.execute(f"""select * from school where roll_no like {roll}""")
                a = cur.fetchall()
                for i in a:
                    print(i)
                
            else:
                print("Wrong bases")

            task = input("Do u want to continue searching data??\n")
    
    elif what_main == "4":
        while task == "y":
            bases_of_del = input("\nhow u want to delete\nPress 1 to delete using Admission no\nPress 2 to delete using name\nPress 3 to delete using class\nPress 4 to delete using roll no\nPress 5 to delete whole data\n") 
            if bases_of_del == "1":
                adno = int(input("Enter Admission NO  :  "))
                cur.execute(f"""Delete from school where Adm_no like {adno}""")
                db.commit()
                
            elif bases_of_del == "2":
                naam = input("Enter Name :  ")
                cur.execute(f"""Delete from school where Name like '{naam}'""")
                db.commit()
                
            elif bases_of_del == "3":
                kaksha = input("Enter Class  :  ")
                cur.execute(f"""Delete from school where class like '{kaksha}'""")
                db.commit()
                
            elif bases_of_del == "4":
                roll = int(input("Enter Roll NO  :  "))                
                cur.execute(f"""Delete from school where roll_no like {roll}""")
                db.commit()

            elif bases_of_del == "5":
                cur.execute(f"""Delete from school""")
                db.commit()    
            else:
                print("Wrong bases")

            task = input("Do u want to continue deleting data??\n")
    
    else:
        print("\t\tWrong Input !!! try again")
    run = input("Do u want to continue Prog??\n")
print("Thx for using a small Programe\n\t\t\t-By DHARUL")
sleep(3)