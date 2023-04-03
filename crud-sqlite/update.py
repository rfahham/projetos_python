mycursor = mydb.cursor()
sql = ''''UPDATE customers SET address = "Canyon 125 WHRE adress = "Valley 345" '''

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")