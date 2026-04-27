import shutil
import time
from datetime import datetime
from pathlib import Path

import schedule


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = BASE_DIR / "backup"

SOURCE_FILE = DATA_DIR / "important.txt"

backup_count = 0
MAX_BACKUPS = 3


def backup_file() -> None:
    """
    Create a timestamped backup copy of the source file.

    This simulates a scheduled automation task.
    """

    global backup_count

    BACKUP_DIR.mkdir(exist_ok=True)

    if not SOURCE_FILE.exists():
        print(f"Source file not found: {SOURCE_FILE}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file_name = f"important_backup_{timestamp}.txt"
    destination_file = BACKUP_DIR / backup_file_name

    shutil.copy(SOURCE_FILE, destination_file)

    backup_count += 1

    print(f"Backup {backup_count} created: {destination_file.name}")


def main() -> None:
    """
    Schedule the backup job to run every 5 seconds.

    For demo purposes, the script stops after 3 backups.
    In a real workflow, this could run continuously or be handled by a scheduler.
    """

    print("Starting scheduled file backup automation...")
    print("Backup job will run every 5 seconds.")
    print("Demo will stop after 3 backups.\n")

    schedule.every(5).seconds.do(backup_file)

    while backup_count < MAX_BACKUPS:
        schedule.run_pending()
        time.sleep(1)

    print("\nScheduled backup demo completed.")


if __name__ == "__main__":
    main()
