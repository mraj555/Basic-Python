import mysql.connector

# Command For Connect MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ambaliya555",
    database="sakila"
)

print(mydb)

mycursor = mydb.cursor()

# Command For Create Database in MySQL
# mycursor.execute("CREATE DATABASE pythonprogramming")

# Command For Get All Databases Of MySQL
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

# Command For Create Table in Database
# mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")

# Command For Show Table
mycursor.execute("SELECT * FROM actor")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
