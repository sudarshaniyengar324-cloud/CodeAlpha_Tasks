import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

cursor.execute(query)

user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()