import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_db"  # Add this if no error meaning database exist
)

mycursor = db.cursor()

# Insert table from database
mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if table exist
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# Create table with auto increment and primary key to id column
mycursor.execute(
    "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Add column to table
mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
