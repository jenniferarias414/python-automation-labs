# Python Automation Labs

## Overview

This repository contains mini-projects built while learning Python automation fundamentals.

Each folder focuses on a practical automation concept using small, hands-on projects that simulate real-world tasks such as file handling, data transformation, reporting, scheduling, notifications, SQL analysis, and workflow reliability.

The goal is to build clean, professional projects that reinforce Python skills while connecting them to data engineering, analytics engineering, and business use cases.

---

## Current Labs

### 01 File Organizer

Automates file organization by scanning a directory, identifying file extensions, and moving files into categorized folders.

**Concepts:**
- `pathlib`
- `shutil`
- File system automation

---

### 02 Regex Log Parser

Reads log files and uses regular expressions to extract timestamps and error messages.

**Concepts:**
- `re`
- Pattern matching
- Text parsing
- Log analysis

---

### 03 Robust File Processor

Processes files safely using logging, assertions, and exception handling.

**Concepts:**
- `try` / `except`
- `logging`
- Assertions
- Defensive programming

---

### 04 Excel Monthly Report Generator

Reads Excel data, calculates totals, and generates a formatted report using Python.

**Concepts:**
- `openpyxl`
- Spreadsheet automation
- Reporting workflows

---

### 05 CSV to JSON Transformer

Converts structured CSV data into JSON format for downstream systems and APIs.

**Concepts:**
- `csv`
- `json`
- Data transformation
- File format conversion

---

### 06 Scheduled File Backup

Creates recurring timestamped backup copies of an important file using a scheduled Python job.

**Concepts:**
- `schedule`
- `datetime`
- `time`
- `shutil`
- Job scheduling
- Recurring automation

---

### 07 Flight Status Email Automation

Reads flight operations data, identifies delayed or cancelled flights, and generates an automated email alert using Gmail SMTP.

**Concepts:**
- `smtplib`
- `imaplib`
- `EmailMessage`
- `.env` configuration
- SMTP email delivery
- IMAP retrieval
- Alert automation
- Secure credential handling

---

### 08 Baggage Claim SQL Lineage Tool

Parses airline baggage-claims SQL queries and maps output columns back to their source tables and source columns using a Streamlit app.

**Concepts:**
- `streamlit`
- `sqlglot`
- `pandas`
- SQL parsing
- Column lineage
- Table aliases
- Metadata analysis
- CSV export

---

## Technologies Used

- Python
- pathlib
- shutil
- re
- logging
- openpyxl
- csv
- json
- schedule
- datetime
- time
- smtplib
- imaplib
- streamlit
- sqlglot
- pandas

---

## Why This Repository Exists

This repository was created to practice practical Python automation patterns commonly used in:

- Data engineering
- Analytics engineering
- ETL workflows
- Reporting automation
- File processing
- Data transformation
- Scheduled jobs
- Operational automation
- Notification systems
- Secure credential workflows
- Metadata analysis
- SQL debugging
- General business automation

---

## Future Labs

Additional automation projects will be added as new concepts are learned, including threading, APIs, web scraping, database automation, cloud integrations, dashboarding, and more advanced workflow orchestration.
