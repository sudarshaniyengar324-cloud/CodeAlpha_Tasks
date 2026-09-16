# CodeAlpha Cyber Security Internship Tasks

This repository contains my completed projects for the **CodeAlpha Cyber Security Internship**.

## Completed Tasks

### Task 1 — Basic Network Sniffer

A Python-based network sniffer developed using **Scapy** to capture and analyze network packets.

**Features:**
- Captures live network packets
- Displays source and destination IP addresses
- Identifies network protocols
- Displays relevant packet information
- Provides basic packet analysis

**Technologies Used:**
- Python
- Scapy
- Npcap

📁 Project folder: `Task_1_Network_Sniffer`

---

### Task 3 — Secure Coding Review

A secure coding review of a Python login application, focusing on identifying and fixing common security vulnerabilities.

**Vulnerabilities Identified:**
- SQL Injection
- Plaintext password storage

**Security Improvements:**
- Parameterized SQL queries
- Salted PBKDF2 password hashing
- Improved database handling
- Secure password storage

**Technologies Used:**
- Python
- SQLite
- hashlib
- secrets
- PBKDF2

📁 Project folder: `Task_3_Secure_Coding_Review`

---

## Repository Structure

```text
CodeAlpha_Tasks/
│
├── Task_1_Network_Sniffer/
│   ├── network_sniffer.py
│   └── README.md
│
└── Task_3_Secure_Coding_Review/
    ├── vulnerable_app.py
    ├── secure_app.py
    ├── secure_password_app.py
    ├── setup_db.py
    ├── security_review.md
    ├── README.md
    └── .gitignore
