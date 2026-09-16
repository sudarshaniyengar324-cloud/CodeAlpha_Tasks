import sqlite3
import hashlib
import secrets


def hash_password(password):
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return salt.hex(), password_hash.hex()


username = input("Enter username: ")
password = input("Enter password: ")

salt, password_hash = hash_password(password)

connection = sqlite3.connect("secure_users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users_secure (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    salt TEXT,
    password_hash TEXT
)
""")

try:
    cursor.execute(
        "INSERT INTO users_secure (username, salt, password_hash) VALUES (?, ?, ?)",
        (username, salt, password_hash)
    )
    connection.commit()
    print("User created with salted PBKDF2 password hash.")
except sqlite3.IntegrityError:
    print("Username already exists.")

connection.close()