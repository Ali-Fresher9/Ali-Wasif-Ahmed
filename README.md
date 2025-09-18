# Ali-Wasif-Ahmed
Assignment-2
===========================================
   File Organizer - Python Automation
===========================================

This project automatically organizes files by DATE and FILE TYPE.
It scans the source folder every minute and moves files into:

   DEST_BASE_DIR / <YYYY-MM-DD> / <FileType> / filename.ext

Example: ( You can use the given example folder for testing)
   Example/
      Organized/
         2025-09-18/
             jpg/
                 photo.jpg
             pdf/
                 notes.pdf
             docx/
                 report.docx

-------------------------------------------
1. Requirements
-------------------------------------------
- Python 3.8 or newer
- Works on Windows, Linux, macOS
- Uses only built-in libraries:
    os, shutil, time, datetime

(Optional)
- You can install "schedule" for cleaner job scheduling:
    pip install schedule

-------------------------------------------
2. Setup
-------------------------------------------
1. Place the script (New.py) anywhere you like.
2. Edit the configuration section in the script:

   SOURCE_DIR = "C:/Users/USERAS/Downloads/Example"
   DEST_BASE_DIR = "C:/Users/USERAS/Downloads/Example/Organized"

   - SOURCE_DIR: folder where your unorganized files are stored.
   - DEST_BASE_DIR: root folder where organized files will be created

   IMPORTANT: 
   Use forward slashes (/) or raw strings (r"...") in Windows paths.

3. Add or update FILE_TYPES inside the script if you want to support
   more extensions:

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

-------------------------------------------
3. Running the Script
-------------------------------------------
Open a terminal (CMD/PowerShell) and run:

   python New.py

The script will:
- Print "Starting organizer..."
- Scan SOURCE_DIR every 60 seconds
- Move files into /Organized/YYYY-MM-DD/<FileType>/

-------------------------------------------
4. Behavior Details
-------------------------------------------
- Date folder is based on the file's LAST MODIFICATION DATE.
- If a file with the same name already exists, the script appends
  a timestamp to the filename (to avoid overwriting).
- Files with unknown extensions go into an "others" folder.
- Subfolders are created automatically if missing.

-------------------------------------------
5. Example Workflow
-------------------------------------------
Before running:
   Example/
      photo.jpg
      report.docx
      notes.pdf

After running:
   Example/
      Organized/
         2025-09-18/
             jpg/
                 photo.jpg
             docx/
                 report.docx
             pdf/
                 notes.pdf

-------------------------------------------
6. Improvements (Optional)
-------------------------------------------
- Use "watchdog" library for real-time organization (instead of every 60s).
- Use "logging" module to log moves into a file.
- Customize DATE_FORMAT (default: YYYY-MM-DD).
- Add "others" folder to catch unrecognized file types.

-------------------------------------------
7. Notes
-------------------------------------------
- The script MOVES files, not copies them.
- Make sure no critical files are accidentally moved.
- You can stop the script anytime with CTRL+C.
