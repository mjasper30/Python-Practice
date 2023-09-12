import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_db"  # Add this if no error meaning database exist
)

mycursor = db.cursor()

# Create database
mycursor.execute("CREATE DATABASE mydatabase")

# Show all database exists
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)