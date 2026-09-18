from pathlib import Path
from tkinter import filedialog
import tkinter as tk
import shutil
import causework as cw

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
    ".exe": "Executable Files",
    ".rar":"Archives",
    ".log":"logs",
    ".pptx":"Presentation Files",
    ".ppsx":"Presentation Files",
    ".potx":"Presentation Files",
    ".json":"Data Files",
    ".xml":"Data Files",
    ".zip":"Archives",
    ".7z":"Archives"
}

def opening():
    print(25*"="+" File Manger System "+25*"=")

def select_folder():

    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory()

    if not folder:
        raise SystemExit

    print("\nYou select: ",folder)

    return folder

def permission(folder):
    print("\nThe following files will be moved to their respective folders:\n")
    pcount = 1

    for file in Path(folder).iterdir():
        if file.is_file():
            key = file.suffix.lower()
            if key in category:
                print(file.name+"-->"+category[key])

            elif key in photo:

                print(file.name+"-->"+"Photos as Photo_",pcount,file.suffix)
                pcount+=1

            else:
                print(file.name+"-->"+"Others")

    per = input("\nDo you want to move? (y/n): ")

    return per.lower()


def work(folder,count):
    print("\nWORKING....")

    pcount = 1

    for file in Path(folder).iterdir():
        if file.is_file():
            key = file.suffix.lower()
            if key in category:
                cut = Path(folder) / category[key]
                cut.mkdir(parents=True,exist_ok=True)
                try:
                    shutil.move(str(file),str(cut/file.name))
                    print(file.name+"-->"+category[key]+", Successfully!")
                    count+=1
                except:
                    print("Error, ",file.name," never move.")
                    
            elif key in photo:
                cut = Path(folder)/ "Photos"
                cut.mkdir(parents=True,exist_ok=True)
                try:
                    rename = f"Photo_{pcount}{file.suffix}"
                except:
                    print(f"Error!, {file.name} never rename as photo_{pcount}{file.suffix}, try to move current name.")
                    shutil.move(str(file),str(cut / file.name))

                try:
                    shutil.move(str(file),str(cut / rename))
                    print(file.name+"-->"+"Photos as Photo_",pcount,file.suffix+", Successfully!")
                    count+=1                
                    pcount+=1
                except:
                    print("Error, ",file.name," never move.")
                    
            else:
                cut = Path(folder) / "Others"
                cut.mkdir(parents=True,exist_ok=True)
                try:
                    shutil.move(str(file),str(cut/file.name))
                    print(file.name+"--> Others, Successfully!")
                    count+=1
                except:
                    print("Error, ",file.name," never move.")

    return count

def ending(folder,count,total):

    print()
    print(25*"="+" Summarize The Task ",25*"=")
    print()

    for fol in Path(folder).iterdir():
        if fol.is_dir():
            print(fol.name+"-->",len(list(fol.iterdir())),"Files")
    
    print("\nTotal files in this folder: ",total)
    print("Total Transferred Files: ",count)
    print()

def cause():
    print("\nNo files were moved. Please enter your cause below:\n\n1. No need close the program\n2. Wrong folder selected\n3.move without some files\n4. Customize folder")
    return input("Enter your cause:")

if __name__ == "__main__":
    opening()

    folder = select_folder()
    total = len(list(Path(folder).iterdir()))
    per = permission(folder)
    count = 0

    if per == "y":
        count = work(folder,count)

    else:
        cnum = cause()
        cw.work(cnum)

    ending(folder,count,total)