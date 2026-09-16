from pathlib import Path
from tkinter import filedialog
import tkinter as tk
import shutil

def opening():
    print(25*"="+" File Manger System "+25*"=")

def select_folder():

    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory()

    if not folder:
        raise SystemExit

    print("You select: ",folder)

    return folder

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
    ".o":"O Files",
    ".exe": "Executable Files"
}

def work(folder):
    print("\nWORKING....")
    count = 0
    for file in Path(folder).iterdir():
        if file.is_file():
            key = file.suffix.lower()
            if key in category:
                cut = Path(folder) / category[key]
                cut.mkdir(parents=True,exist_ok=True)
                shutil.move(str(file),str(cut/file.name))
                print(file.name+"-->"+category[key])
                count+=1


            else:
                cut = Path(folder) / "Others"
                cut.mkdir(parents=True,exist_ok=True)
                shutil.move(str(file),str(cut/file.name))
                print(file.name+"--> Others")
                count+=1

    return count

def ending(folder,count):
    print()
    print(25*"="+" Summarize The Task ",25*"=")
    for fol in Path(folder).iterdir():
        if fol.is_dir():
            print(fol.name+"-->",len(list(fol.iterdir())),"Files")

    print("\nTotal Transferred Files: ",count)
    print()

if __name__ == "__main__":
    opening()
    folder = select_folder()
    count = work(folder)
    ending(folder,count)