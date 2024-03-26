import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tati",
  password="123",
  database= 'pythonML', #optinal
  ssl_disabled=True  # Disable SSL/TLS
)

mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")

# val = ("John", "Highway 21") single value
# mycursor.execute(sql, val) #for single value
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# # mycursor.executemany(sql, val) #for many values
# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)
# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)
#You can also select the records that starts, includes, or ends with a given letter or phrase.Use the %  to represent wildcard characters:
sql=("SELECT * FROM customers WHERE id= %s")
adr = ('1',)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
# delete statment dont forget to commit 
#######################
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()
#######################
#update row
#######################
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()
######################
# myresult = mycursor.fetchone() #you can also use this if the expected data is one
for x in myresult:
  y= list(x)
  print(y)