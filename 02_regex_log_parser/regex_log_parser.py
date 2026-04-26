import re
from pathlib import Path


ERROR_PATTERN = re.compile(
    r"^ERROR - (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)$"
)


def extract_errors(log_file_path: str) -> list[tuple[str, str]]:
    """
    Read a log file and extract ERROR lines.

    Returns:
        A list of tuples containing:
        - timestamp
        - error message
    """
    log_file = Path(log_file_path)
    errors = []

    if not log_file.exists():
        print(f"Log file does not exist: {log_file}")
        return errors

    with log_file.open("r") as file:
        for line in file:
            match = ERROR_PATTERN.search(line.strip())

            if match:
                timestamp = match.group(1)
                message = match.group(2)
                errors.append((timestamp, message))

    return errors


if __name__ == "__main__":
    log_path = "02_regex_log_parser/sample_logs/app.log"

    extracted_errors = extract_errors(log_path)

    print("Extracted ERROR messages:")
    print("-------------------------")

    for timestamp, message in extracted_errors:
        print(f"{timestamp}: {message}")