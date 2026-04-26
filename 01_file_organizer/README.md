# File Organizer Automation

## Overview

This mini-project demonstrates how Python can automate file organization.

The script scans a folder, checks each file extension, and moves files into categorized subfolders such as Images, Documents, Music, Videos, and Others.

## Why This Matters

File organization is a common automation use case. Instead of manually sorting downloaded files, reports, images, or documents, Python can apply consistent rules and organize them automatically.

## How It Works

1. Define file categories by extension
2. Loop through files in a target folder
3. Determine each file's category
4. Create the destination folder if needed
5. Move the file into the correct folder

## Concepts Demonstrated

- `Path` objects from `pathlib`
- Checking file extensions
- Creating folders
- Moving files with `shutil.move`
- Writing reusable functions
- Using `if __name__ == "__main__"`

## How to Run

From the root of the repository:

python 01_file_organizer/file_organizer.py

## Example Result

Before:

sample_files/
- photo1.jpg
- report.pdf
- notes.txt
- song.mp3
- random_file.xyz

After:

sample_files/
- Images/photo1.jpg
- Documents/report.pdf
- Documents/notes.txt
- Music/song.mp3
- Others/random_file.xyz

![File Organizer Output](screenshots/01_file_organizer_result.png)

## Alternative Implementation (os module)

This project also includes an implementation using Python’s built-in `os` and `shutil` modules.

Why this matters:
- Demonstrates low-level file system control
- Common in legacy scripts and automation jobs
- Useful for ETL-style file movement tasks

Two approaches included:
1. Modern approach (cleaner, easier to read)
2. OS-based approach (more control, more verbose)

## Key Takeaway

Python automation is useful for repetitive file management tasks because it can apply consistent rules quickly and reduce manual effort.