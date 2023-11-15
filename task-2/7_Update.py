import mysql.connector


con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234", database="pythondb")
mycursor = con.cursor()


mycursor.execute("update employeeInfo set Salary=60000 where Emp_ID=102")

con.commit()