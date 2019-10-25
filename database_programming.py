import sqlite3

conn = sqlite3.connect('test3.db')

print ("Opened database successfully")
try:
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
except sqlite3.OperationalError:
    pass
#print "Table created successfully";
def insert():
    print("---------INSERT INTO COMPANY TABLE------------")
    n=int(input("enter number of employees"))
    for i in range(n):
        print("enter name,address,salary for emp ",i,":")
        name=input()
        address=input()
        salary=float(input())
    try:
        conn.execute("INSERT INTO COMPANY (NAME,ADDRESS,SALARY) \
      VALUES (?,?,?)",(name,address,salary))
    except sqlite3.IntegrityError:
        pass
    print ("inserted into Table successfully");
    conn.commit()
def display():
    print("---------EMPLOYEE INFORMATION------------")

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
def spec_emp():  
    print("-----------SPECIFIC EMPLOYEE INFO-------------")
    i1=int(input("enter id of employee: "))
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY where id='{}'".format(i1))
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
def update():  
    print("---------UPDATE EMPLOYEE DATA------------")
    n=int(input("enter id of empoyee: "))
    sal=float(input("enter updated salary: "))
    conn.execute("UPDATE COMPANY set SALARY ='{}'where ID ='{}'",format(sal),format(n))
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
def delete():  
    print("---------DELETE EMPLOYEE INFO------------")
    n=int(input("enter id of empoyee: "))
    conn.execute("DELETE from COMPANY where ID = ?;",n)
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")

print("1.INSERT\n2.DISPLAY\n3.RETREIVE SPECIFIC EMPLOYEE\n4.UPDATE\n5.DELETE\n")
def choice(i):
    switcher={1:insert,2:display,3:spec_emp,4:update,5:delete}
    func=switcher.get(i,lambda:'invalid')
    return func()
while(1):
    c=int(input("enter your choice: "))
    choice(c)

