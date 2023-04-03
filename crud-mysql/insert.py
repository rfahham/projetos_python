mycursor = mydb.cursor()

sql = "INSERT INTO sustomers (name, addres) VALUES(%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)
mydb.commit()

