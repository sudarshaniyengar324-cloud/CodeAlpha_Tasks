\# Secure Coding Review — CodeAlpha Task 3



\## 1. Project Overview



This project demonstrates a secure coding review of a Python login application using SQLite.



The review compares an intentionally vulnerable version with an improved secure version. The main security issues identified were SQL Injection and insecure plaintext password storage.



\## 2. Technologies Used



\* Python 3

\* SQLite

\* Python `sqlite3` module

\* Python `hashlib` module

\* Python `secrets` module



\## 3. Vulnerability 1 — SQL Injection



\### Description



The vulnerable application directly concatenates user-supplied username and password values into an SQL query.



\### Vulnerable Code



```python

query = "SELECT \* FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

cursor.execute(query)

```



\### Security Risk



Because user input is directly combined with the SQL statement, specially crafted input could alter the intended SQL query.



Potential impacts include:



\* Unauthorized authentication

\* Exposure or manipulation of database information

\* Bypassing application security controls



\### Severity



\*\*High\*\*



\### Recommended Remediation



Use parameterized SQL queries instead of directly concatenating user input.



\### Secure Code



```python

query = "SELECT \* FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))

```



Parameterized queries keep user input separate from the SQL command and help prevent SQL injection.



\---



\## 4. Vulnerability 2 — Plaintext Password Storage



\### Description



The original test database stored the user's password directly as plaintext.



\### Example



```python

("Sudu", "test123")

```



\### Security Risk



If an attacker obtains the database, plaintext passwords can be immediately read and potentially reused on other services.



\### Severity



\*\*High\*\*



\### Recommended Remediation



Passwords should not be stored as plaintext. A password-specific, salted hashing approach should be used.



\### Secure Implementation



The improved application uses:



\* A randomly generated salt

\* PBKDF2-HMAC-SHA256

\* 100,000 iterations

\* A stored password hash instead of the original password



Example:



```python

salt = secrets.token\_bytes(16)



password\_hash = hashlib.pbkdf2\_hmac(

&#x20;   "sha256",

&#x20;   password.encode(),

&#x20;   salt,

&#x20;   100000

)

```



The database stores the salt and derived password hash rather than the original password.



\---



\## 5. Security Improvements



| Area                | Vulnerable Version          | Secure Version                 |

| ------------------- | --------------------------- | ------------------------------ |

| SQL queries         | String concatenation        | Parameterized queries          |

| Password storage    | Plaintext                   | Salted PBKDF2 hash             |

| User input handling | Directly inserted into SQL  | Passed as query parameters     |

| Database security   | Vulnerable to SQL injection | SQL injection protection added |



\## 6. Testing



The vulnerable application was tested using a local SQLite database.



A valid test account successfully demonstrated the intended login functionality.



The secure application was then tested using the same type of login functionality and successfully authenticated the test user.



The improved password-storage implementation was also verified by checking the database contents. The original password was not stored directly; instead, a salt and password hash were stored.



\## 7. Conclusion



The code review identified two important security weaknesses:



1\. SQL Injection caused by unsafe SQL string construction.

2\. Plaintext password storage.



The vulnerabilities were addressed by using parameterized SQL queries and salted PBKDF2 password hashing.



This project demonstrates how secure coding practices can reduce common application security risks and protect user information.



\## 8. Future Improvements



For a production application, additional security improvements could include:



\* Account lockout or rate limiting

\* Secure session management

\* Multi-factor authentication

\* HTTPS/TLS

\* Strong password policies

\* Secure logging and monitoring

\* A production-grade password hashing configuration such as Argon2id

\* Proper secret and credential management



