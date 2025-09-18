import os
import shutil
import time
from datetime import datetime
import threading

# CONFIGURATION
SOURCE_DIR = "C:/Users/USERAS/Downloads/Example"   # e.g. Source file
DEST_BASE_DIR = "C:/Users/USERAS/Downloads/Example"    # root where organized structure will go
FILE_TYPES = {
    ".jpg": "jpg",
    ".jpeg": "jpg",
    ".png": "png",
    ".gif": "gif",
    ".pdf": "pdf",
    ".docx": "docx",
    ".doc": "doc",
    # add more as needed
}

DATE_FORMAT = "%Y-%m-%d"   # Format for date folder, e.g. 2025-09-18

def organize_once():
    for fname in os.listdir(SOURCE_DIR):
        src_path = os.path.join(SOURCE_DIR, fname)
        if not os.path.isfile(src_path):
            # skip directories
            continue

        # get the file extension (lowercase)
        _, ext = os.path.splitext(fname)
        ext = ext.lower()
        if ext not in FILE_TYPES:
            # you may want to skip or put into "others"
            filetype = "others"
        else:
            filetype = FILE_TYPES[ext]

        # choose the date: modification time
        mtime = os.path.getmtime(src_path)
        date = datetime.fromtimestamp(mtime).strftime(DATE_FORMAT)

        # build destination folder
        dest_dir = os.path.join(DEST_BASE_DIR, date, filetype)
        os.makedirs(dest_dir, exist_ok=True)

        # build the destination path
        dest_path = os.path.join(dest_dir, fname)

        # if file with same name exists in dest, you may want to rename or skip
        if os.path.exists(dest_path):
            # e.g. append timestamp or something
            base, extension = os.path.splitext(fname)
            new_name = f"{base}_{int(time.time())}{extension}"
            dest_path = os.path.join(dest_dir, new_name)

        # move the file
        try:
            shutil.move(src_path, dest_path)
            print(f"Moved: {fname} -> {dest_path}")
        except Exception as e:
            print(f"Error moving file {fname}: {e}")

def run_continuously(interval_seconds=60):
    """
    Run organize_once every `interval_seconds`. This is a simple scheduler.
    """
    while True:
        try:
            organize_once()
        except Exception as e:
            print(f"Error in organize_once: {e}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    print("Starting organizer...")
    run_continuously(interval_seconds=60)
