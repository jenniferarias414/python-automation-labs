import logging
from pathlib import Path


# Set up logging so the program gives useful status messages while it runs.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def process_file(file_path: Path) -> dict | None:
    """
    Reads a text file, counts words/lines, and logs the result.

    This function is intentionally defensive:
    - It checks whether the file exists.
    - It handles empty files.
    - It catches unexpected errors instead of crashing the program.
    """

    if not file_path.exists():
        logging.error(f"File does not exist: {file_path.name}")
        return None

    try:
        content = file_path.read_text()

        line_count = len(content.splitlines())
        word_count = len(content.split())

        # Assertion = sanity check.
        # If this assumption is false, Python raises an AssertionError.
        assert word_count >= 0, "Word count should never be negative."

        if word_count == 0:
            logging.warning(f"File is empty: {file_path.name}")
        else:
            logging.info(
                f"Processed {file_path.name}: {line_count} lines, {word_count} words"
            )

        return {
            "file_name": file_path.name,
            "line_count": line_count,
            "word_count": word_count,
            "status": "processed"
        }

    except PermissionError:
        logging.error(f"Permission denied while reading file: {file_path.name}")
        return None

    except AssertionError as error:
        logging.error(f"Assertion failed for {file_path.name}: {error}")
        return None

    except Exception as error:
        logging.error(f"Unexpected error while processing {file_path.name}: {error}")
        return None


def write_summary(results: list[dict]) -> None:
    """
    Writes a small summary report to the output folder.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    summary_path = OUTPUT_DIR / "processing_summary.txt"

    with summary_path.open("w") as summary_file:
        summary_file.write("Robust File Processor Summary\n")
        summary_file.write("=============================\n\n")

        for result in results:
            summary_file.write(f"File: {result['file_name']}\n")
            summary_file.write(f"Lines: {result['line_count']}\n")
            summary_file.write(f"Words: {result['word_count']}\n")
            summary_file.write(f"Status: {result['status']}\n")
            summary_file.write("\n")

    logging.info(f"Summary report written to: {summary_path}")


def main() -> None:
    """
    Main project workflow.
    """

    files_to_process = [
        DATA_DIR / "sample_log.txt",
        DATA_DIR / "empty_file.txt",
        DATA_DIR / "missing_file.txt"
    ]

    successful_results = []

    for file_path in files_to_process:
        result = process_file(file_path)

        if result is not None:
            successful_results.append(result)

    write_summary(successful_results)


if __name__ == "__main__":
    main()