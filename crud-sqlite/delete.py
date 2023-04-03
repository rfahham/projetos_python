mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)
mydb.commit()

