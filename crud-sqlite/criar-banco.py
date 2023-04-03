import sqlite3

conection = sqlite3.connect('mydb-crud.db')

cursor = conection.cursor()

cursor.execute("""CREATE TABLE crudb (
    nome text,
    idade interger
)""")
               
conection.commit()

conection.close()