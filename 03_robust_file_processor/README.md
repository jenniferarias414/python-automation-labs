Robust File Processor
Objective

This project demonstrates core Python debugging and error-handling concepts by building a robust file processor that can handle missing files, empty files, and unexpected file-processing issues without crashing.

The goal is to practice:

Exception handling with try / except
Assertions for sanity checks
Logging with different message levels
Defensive programming for automation scripts
Writing a simple processing summary
What This Project Does

This script processes text files from a local data/ folder and creates a summary report in an output/ folder.

For each file, the script:

Checks whether the file exists
Reads the file content
Counts the number of lines
Counts the number of words
Logs success, warning, or error messages
Writes successful processing results to a summary file
Why This Matters

In real-world data engineering, pipelines often process files from systems like S3, shared drives, APIs, or landing zones.

File processing can fail for many reasons:

The file does not exist
The file is empty
The file has unexpected content
The system does not have permission to read the file
A transformation fails during processing

Instead of allowing the entire program to crash, robust scripts should log useful information, handle known issues gracefully, and continue processing where possible.

Project Structure
03_robust_file_processor/
├── data/
│   ├── sample_log.txt
│   └── empty_file.txt
├── output/
│   └── processing_summary.txt
├── screenshots/
├── robust_file_processor.py
└── README.md
Key Concepts
Exception Handling

Exception handling allows the program to catch and respond to errors instead of crashing immediately.

try:
    content = file_path.read_text()
except Exception as error:
    logging.error(f"Unexpected error: {error}")
Assertions

Assertions are used to check assumptions in code.

assert word_count >= 0, "Word count should never be negative."

In this project, the assertion confirms that the word count calculation produced a valid result.

Logging

Logging records what the program is doing while it runs.

logging.info("File processed successfully")
logging.warning("File is empty")
logging.error("File does not exist")

Logging is more professional than using only print() because it supports different severity levels and is easier to use in production-style scripts.

How to Run
python 03_robust_file_processor/robust_file_processor.py
Example Terminal Output
INFO - Processed sample_log.txt: 5 lines, 37 words
WARNING - File is empty: empty_file.txt
ERROR - File does not exist: missing_file.txt
INFO - Summary report written to: output/processing_summary.txt
Example Summary Output
Robust File Processor Summary
=============================

File: sample_log.txt
Lines: 5
Words: 37
Status: processed

File: empty_file.txt
Lines: 0
Words: 0
Status: processed
Screenshots
Project Structure

Terminal Logs

Summary Output

Python Code

Key Takeaways
Debugging is the process of finding, understanding, and fixing problems in code
try / except blocks help prevent programs from crashing when expected errors occur
Assertions help validate assumptions during development
Logging provides visibility into what a script is doing and makes troubleshooting easier
Robust file processing is an important pattern in data engineering pipelines
Real-World Data Engineering Connection

This project simulates a small but important part of a data pipeline: safely processing incoming files.

In production, this pattern is used when:

Ingesting files from cloud storage (e.g., S3)
Validating incoming data
Logging pipeline events
Handling failures without breaking entire workflows
Generating summaries for monitoring and debugging
