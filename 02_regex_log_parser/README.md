# Robust File Processor

## Overview

This mini-project demonstrates how Python debugging tools can be used to build a more reliable file-processing script.

The script reads text files from a `data/` folder, counts lines and words, handles common file issues, logs what happened, and writes a small processing summary.

## Why This Matters

File processing is common in data engineering, automation, ETL jobs, cloud workflows, and pipeline monitoring.

Real-world files are not always perfect. A script may run into:

- Missing files
- Empty files
- Permission errors
- Unexpected content
- Processing errors

Instead of crashing, a reliable script should log the issue, continue where possible, and create useful output for debugging.

## What This Project Covers

This project practices the same debugging concepts from the Python Automation module:

- `try` / `except`
- Exception handling
- `assert`
- Assertions for sanity checks
- `logging` module
- Logging levels such as `INFO`, `WARNING`, and `ERROR`
- File existence checks
- Writing a processing summary

## Project Structure

![Project Structure](screenshots/01_project_structure.png)

## Key Debugging Concepts

### Exception Handling

Exception handling lets the program respond to errors instead of crashing immediately.

Example:

`try:`

`    content = file_path.read_text()`

`except Exception as error:`

`    logging.error(f"Unexpected error: {error}")`

### Assertions

Assertions check assumptions during development.

Example:

`assert word_count >= 0, "Word count should never be negative."`

In this project, the assertion confirms that the word count calculation produced a valid result.

### Logging

Logging records what the program is doing while it runs.

Example:

`logging.info("File processed successfully")`

`logging.warning("File is empty")`

`logging.error("File does not exist")`

Logging is more professional than only using `print()` because it supports severity levels and is easier to use in production-style scripts.

## How It Works

1. Define the files that should be processed
2. Check whether each file exists
3. Read the file content
4. Count lines and words
5. Use an assertion to validate the result
6. Log successful files, empty files, and missing files
7. Store successful processing results
8. Write a summary report to the `output/` folder

## How to Run

From the root of the repository:

`python3 03_robust_file_processor/robust_file_processor.py`

## Example Terminal Output

```text
INFO - Processed sample_log.txt: 5 lines, 37 words
WARNING - File is empty: empty_file.txt
ERROR - File does not exist: missing_file.txt
INFO - Summary report written to: output/processing_summary.txt
```

### Terminal Logs Screenshot

![Terminal Logs](screenshots/02_terminal_logs.png)

## Example Summary Output

```text
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
```

### Summary Output Screenshot

![Summary Output](screenshots/03_summary_output.png)

## Code Example

The main debugging logic uses file checks, exception handling, assertions, and logging.

### Python Code Screenshot

![Python Code](screenshots/04_python_code.png)

## Key Takeaway

Debugging is not just fixing broken code. It is also about making scripts easier to understand, monitor, and recover from when something goes wrong.

Robust scripts should:

- Detect issues early
- Log useful information
- Avoid crashing when possible
- Continue processing valid inputs
- Create output that helps with troubleshooting

In data engineering, this pattern is important because pipelines often depend on files arriving correctly, being readable, and containing usable data.

## Real-World Data Engineering Connection

This project simulates a small file ingestion step in a data pipeline.

In production, similar logic could be used when:

- Processing files from S3 or a data lake
- Validating incoming datasets
- Logging pipeline events
- Skipping bad files while continuing with good files
- Creating processing summaries for monitoring
- Debugging failed ETL or automation jobs
