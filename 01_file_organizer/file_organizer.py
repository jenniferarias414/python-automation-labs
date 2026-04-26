from pathlib import Path
import shutil


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
}


def organize_files(directory: str) -> None:
    source_dir = Path(directory)

    if not source_dir.exists():
        print(f"Directory does not exist: {source_dir}")
        return

    for file_path in source_dir.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            category = "Others"

            for folder_name, extensions in FILE_TYPES.items():
                if extension in extensions:
                    category = folder_name
                    break

            target_dir = source_dir / category
            target_dir.mkdir(exist_ok=True)

            target_path = target_dir / file_path.name
            shutil.move(str(file_path), str(target_path))

            print(f"Moved {file_path.name} → {category}/")


if __name__ == "__main__":
    organize_files("01_file_organizer/sample_files")