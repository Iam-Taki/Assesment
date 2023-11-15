import mysql.connector
con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234")

mycursor = con.cursor()

mycursor.execute("show databases")
for db in mycursor:
    print(db)