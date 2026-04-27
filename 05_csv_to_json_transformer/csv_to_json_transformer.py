import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_FILE = DATA_DIR / "orders.csv"
OUTPUT_FILE = OUTPUT_DIR / "orders.json"


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    """
    Convert CSV rows into a JSON file.

    Each CSV row becomes one dictionary.
    The final JSON output becomes a list of dictionaries.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    records = []

    with csv_file.open("r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Skip rows that are completely empty.
            if not any(row.values()):
                continue

            records.append(row)

    with json_file.open("w") as file:
        json.dump(records, file, indent=4)

    print(f"Converted {len(records)} records from CSV to JSON")
    print(f"JSON file created: {json_file}")


if __name__ == "__main__":
    csv_to_json(INPUT_FILE, OUTPUT_FILE)
