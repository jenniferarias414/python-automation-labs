# Regex Log Parser

## Overview

This mini-project demonstrates how Python regular expressions can be used to extract structured information from unstructured text.

The script reads a sample application log file, identifies lines that begin with `ERROR`, and extracts two useful pieces of information:

- Timestamp
- Error message

## Why This Matters

Log files are common in data engineering, application support, ETL jobs, cloud workflows, and pipeline monitoring.

Manually searching logs is slow and error-prone. Regex allows us to automate pattern matching so important information can be extracted quickly and consistently.

## What This Project Covers

This project practices the same regex concepts from the Python Automation module:

- `re` module
- `re.compile()`
- Regex objects
- Capture groups with parentheses
- `search()`
- Start/end anchors
- Character classes
- Quantifiers
- Extracting structured values from text

## Regex Pattern Used

Pattern:

`^ERROR - (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)$`

## Pattern Breakdown

| Pattern Part | Meaning |
|---|---|
| `^` | Start of the line |
| `ERROR - ` | Match only lines beginning with ERROR |
| `(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})` | Capture the timestamp |
| `.*` | Capture the rest of the line as the error message |
| `$` | End of the line |

## Example Log Input

`ERROR - 2026-04-26 08:02:30 - Failed to connect to database`

## Extracted Output

Timestamp:

`2026-04-26 08:02:30`

Message:

`Failed to connect to database`

## How It Works

1. Open the log file
2. Read each line
3. Use regex to search for ERROR lines
4. Capture the timestamp and message
5. Store the results in a list of tuples
6. Print the extracted errors

## How to Run

From the root of the repository:

`python3 02_regex_log_parser/regex_log_parser.py`

## Example Result

```text
Extracted ERROR messages:
-------------------------
2026-04-26 08:02:30: Failed to connect to database
2026-04-26 08:04:12: Missing required field: customer_id
2026-04-26 08:05:44: File not found: orders.csv
```

### Screenshot

![Regex Log Parser Result](screenshots/01_regex_log_parser_result.png)

## Key Takeaway

Regex is useful when text has a predictable pattern but is not already structured as rows and columns.

In data engineering, this can be used for:
- Parsing logs
- Extracting IDs
- Validating file names
- Checking timestamps
- Identifying failed pipeline events

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
