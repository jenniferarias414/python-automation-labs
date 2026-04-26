import os
import shutil

def organize_files(directory):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Others': []
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in file_types.items():
                if ext in extensions:
                    target_dir = os.path.join(root, category)
                    os.makedirs(target_dir, exist_ok=True)

                    shutil.move(
                        os.path.join(root, file),
                        os.path.join(target_dir, file)
                    )
                    moved = True
                    break

            if not moved:
                target_dir = os.path.join(root, 'Others')
                os.makedirs(target_dir, exist_ok=True)

                shutil.move(
                    os.path.join(root, file),
                    os.path.join(target_dir, file)
                )