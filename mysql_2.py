import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tati",
  password="123",
  database="pythonML",
  ssl_disabled=True  # Disable SSL/TLS
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)