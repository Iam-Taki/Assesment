import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="Takihost", passwd="Taki1234")
    mycursor = con.cursor()
    mycursor.execute("CREATE DATABASE pythondb")
    print("Database 'pythondb' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if con.is_connected():
        con.close()


