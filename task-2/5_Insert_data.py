import mysql.connector


con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234", database="pythondb")
mycursor = con.cursor()


mycursor.execute("insert into employeeInfo(Emp_ID,Emp_Name, Designation, Salary) values (101, 'Sakib','Manager',70000)")

insertdata= "insert into employeeInfo(Emp_ID,Emp_Name, Designation, Salary) values (%s,%s,%s,%s)"


#make a tuple

records = [
    (102, "Akash", "Progammer", 50000),
    (103, "Rassel", "Progammer", 40000),
    (104, "Proksh", "Progammer", 30000),
    (105, "Sara", "HR", 50000),
    (106, "Jarin", "HR", 30000),
    (107, "Kabir", "Intern", 10000),
]

mycursor.executemany(insertdata, records)

con.commit()