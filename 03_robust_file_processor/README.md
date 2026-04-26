# Robust File Processor

## Overview

This mini-project demonstrates how to build a resilient Python script that safely processes files while handling common errors.

The script reads text files from a data folder, counts lines and words, and logs results without crashing when issues occur.

---

## Why This Matters

In real-world data engineering, pipelines often process files from external systems such as S3, APIs, or shared storage.

These workflows frequently encounter issues like:

- Missing files  
- Empty files  
- Permission errors  
- Unexpected data  

Instead of failing completely, production systems should **log issues, skip bad inputs, and continue processing**.

---

## What This Project Covers

This project practices core debugging and reliability concepts:

- Exception handling (`try` / `except`)
- Assertions (`assert`)
- Logging (`logging` module)
- File validation before processing
- Writing a simple summary output

---

## Key Concepts

### Exception Handling

Used to prevent crashes when errors occur.

Example:

`try:`
`    content = file_path.read_text()`
`except Exception as error:`
`    logging.error(f"Unexpected error: {error}")`

---

### Assertions

Used to validate assumptions in code.

Example:

`assert word_count >= 0, "Word count should never be negative."`

---

### Logging

Used to track what the script is doing.

Example:

`logging.info("File processed successfully")`  
`logging.warning("File is empty")`  
`logging.error("File does not exist")`  

---

## How It Works

1. Define a list of files to process  
2. Check if each file exists  
3. Read file contents  
4. Count lines and words  
5. Log results (INFO, WARNING, ERROR)  
6. Store successful results  
7. Write a summary report  

---

## How to Run

From the root of the repository:

`python 03_robust_file_processor/robust_file_processor.py`

---

## Example Terminal Output

```text
INFO - Processed sample_log.txt: 5 lines, 37 words
WARNING - File is empty: empty_file.txt
ERROR - File does not exist: missing_file.txt
INFO - Summary report written to: output/processing_summary.txt
```

---

## Example Summary Output

```text
Robust File Processor Summary

File: sample_log.txt Lines: 5 Words: 37 Status: processed
File: empty_file.txt Lines: 0 Words: 0 Status: processed
```

---

## Code Example (Debugging Logic)

---

## Key Takeaway

Robust scripts should not fail when something goes wrong. Instead, they should:

- Detect issues early
- Log useful information
- Continue processing valid inputs

This is a foundational pattern for building reliable automation and data pipelines.

--- 

## Real-World Data Engineering Connection

This project simulates a file ingestion step in a data pipeline.

In production, this pattern is used when:

- Processing files from S3 or data lakes
- Validating incoming datasets
- Logging pipeline activity
- Handling failures without breaking workflows

This is a key skill for debugging and maintaining data pipelines.