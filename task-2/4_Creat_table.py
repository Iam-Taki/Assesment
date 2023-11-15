import mysql.connector

# Connect to the MySQL server and select the 'pythondb' database
con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234", database="pythondb")
mycursor = con.cursor()

# Corrected SQL statement for creating the table
mycursor.execute("CREATE TABLE employeeInfo (Emp_ID INT, Emp_Name VARCHAR(100), Designation VARCHAR(100), Salary DECIMAL(15,2))")
