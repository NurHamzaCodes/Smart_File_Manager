from pathlib import Path
from tkinter import filedialog
import tkinter as tk
import shutil

photo = [".jpg",".png",".jpeg",".gif",".bmp"]

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
    ".o":"O Files",
    ".exe": "Executable Files"
}

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

def permission(folder):
    print("\nThe following files will be moved to their respective folders:\n")
    for file in Path(folder).iterdir():
        if file.is_file():
            key = file.suffix.lower()
            if key in category:
                print(file.name+"-->"+category[key])

            elif key in photo:
                print(file.name+"-->"+"Photos")

            else:
                print(file.name+"-->"+"Others")

    per = input("\nDo you want to move? (y/n): ")

    return per.lower()


def work(folder):
    print("\nWORKING....")

    count = 0
    pcount = 1

    for file in Path(folder).iterdir():
        if file.is_file():
            key = file.suffix.lower()
            if key in category:
                cut = Path(folder) / category[key]
                cut.mkdir(parents=True,exist_ok=True)
                shutil.move(str(file),str(cut/file.name))
                count+=1

            elif key in photo:
                cut = Path(folder)/ "Photos"
                cut.mkdir(parents=True,exist_ok=True)
                rename = f"Photo_{pcount}{file.suffix}"
                shutil.move(str(file),str(cut / rename))
                pcount+=1
                count+=1

            else:
                cut = Path(folder) / "Others"
                cut.mkdir(parents=True,exist_ok=True)
                shutil.move(str(file),str(cut/file.name))
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

def cause():
    print("\nNo files were moved. Please enter your cause below:\n\n1. No need close the program\n2. Wrong folder selected\n3.move without some files\n")
    return input("Enter your cause:")

if __name__ == "__main__":
    opening()
    folder = select_folder()
    per = permission(folder)

    if per == "y":
        count = work(folder)

    else:
        cnum = cause()

    ending(folder,count)