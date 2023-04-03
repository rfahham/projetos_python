mycursor = mydb.cursor()

sql = "INSERT INTO sustomers (name, addres) VALUES(%s, %s)"
val = [
    ("John", "Highway 21"),
    ("Richard", "Sky st 351")
]
mycursor.execute(sql, val)
mydb.commit()

