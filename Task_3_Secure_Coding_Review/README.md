\# CodeAlpha Secure Coding Review



\## Project Overview



This project was created as part of the CodeAlpha Cyber Security Internship.



The project performs a secure coding review of a Python login application and demonstrates how common security vulnerabilities can be identified and remediated.



\## Objectives



\* Review application source code for security vulnerabilities.

\* Identify unsafe coding practices.

\* Demonstrate SQL Injection risk.

\* Demonstrate the risks of plaintext password storage.

\* Implement secure coding improvements.

\* Document the identified vulnerabilities and their remediation.



\## Technologies Used



\* Python 3

\* SQLite

\* Python `sqlite3`

\* Python `hashlib`

\* Python `secrets`



\## Project Structure



```text

Task\_3\_Secure\_Coding\_Review/

│

├── vulnerable\_app.py

├── setup\_db.py

├── secure\_app.py

├── secure\_password\_app.py

├── security\_review.md

├── README.md

└── .gitignore

```



\## Security Issues Identified



\### 1. SQL Injection



The vulnerable application constructs an SQL query by directly concatenating user input.



This can allow specially crafted input to alter the intended SQL query.



\### Remediation



The secure version uses parameterized SQL queries:



```python

query = "SELECT \* FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))

```



\### 2. Plaintext Password Storage



The original implementation stored the test password directly.



This is unsafe because anyone who gains access to the database could read the password.



\### Remediation



The improved implementation uses a randomly generated salt and PBKDF2-HMAC-SHA256 to derive a password hash.



The original password is not stored directly.



\## Testing



The application was tested using a local SQLite database.



The vulnerable and secure versions were both tested with a local test account.



The secure password-storage implementation was also checked to confirm that the password was not stored directly in the database.



\## Security Precautions



This project was developed and tested locally using test credentials and a local SQLite database.



Database files containing test data are excluded from the GitHub repository using `.gitignore`.



\## Conclusion



The project demonstrates how secure coding practices can reduce common application security risks.



The identified issues were addressed using parameterized SQL queries and salted password hashing.



\## Internship Task



\*\*CodeAlpha Cyber Security Internship — Task 3: Secure Coding Review\*\*



