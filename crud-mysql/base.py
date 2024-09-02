# lets start with creating a table in which we will do diffetent operations.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute('''CREATE TABLE customers(name VARCHAR(255), adress VARCHAR(255))''')