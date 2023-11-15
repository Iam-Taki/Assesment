import mysql.connector


con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234", database="pythondb")
mycursor = con.cursor()


mycursor.execute("select * from employeeInfo")

showResult = mycursor.fetchall()

for row in showResult:
    print(row)