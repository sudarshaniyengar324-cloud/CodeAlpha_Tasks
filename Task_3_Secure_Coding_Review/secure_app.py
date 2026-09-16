import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

connection.close()