import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("Sudu", "test123")
)

connection.commit()
connection.close()

print("Test database created successfully!")