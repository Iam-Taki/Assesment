import mysql.connector


con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234", database="pythondb")
mycursor = con.cursor()


mycursor.execute("delete from employeeInfo where Emp_ID = 107 ")

con.commit()
print ("Record Deleted")