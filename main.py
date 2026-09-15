from pathlib import Path
from tkinter import filedialog
import tkinter as tk
import shutil

root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory()

if not folder:
    raise SystemExit

category = {
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".flv": "Videos",
    ".mp3": "Audio Files",
    ".wav": "Audio Files",
    ".pdf": "Books",
    ".html": "Books",
    ".doc": "Text Files",
    ".docx": "Text Files",
    ".txt": "Text Files",
    ".py": "Code Files",
    ".c": "Code Files",
    ".csv": "Excel Files",
    ".xlsx": "Excel Files",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
}

for file in Path(folder).iterdir():
    if file.is_file():
        file_category = category.get(file.suffix.lower(), "Others")
        cut = Path(folder) / file_category
        cut.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(cut / file.name))