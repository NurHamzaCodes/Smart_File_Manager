from pathlib import Path
from tkinter import filedialog
import tkinter as tk
import shutil
import causework as cw
import variable as va

photo = [".jpg",".png",".jpeg",".gif",".bmp"]

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
            if key in va.category:
                print(file.name+"-->"+va.category[key])

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
            if key in va.category:
                cut = Path(folder) / va.category[key]
                cut.mkdir(parents=True,exist_ok=True)
                try:
                    shutil.move(str(file),str(cut/file.name))
                    print(file.name+"-->"+va.category[key]+", Successfully!")
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

    return input("\n\nDo you want to close program(y) or something wrong(n): ")    

def cause():
    print("\nNo files were moved. Please enter your cause below:\n\n1. No need close the program\n2. Wrong folder name\n3. Customize folder for an extention\n")
    return int(input("Enter your cause:"))

def restore(folder):
    for fol in Path(folder).iterdir():
        if fol.is_dir():
            for file in fol.iterdir():
                if fol.is_file():
                    shutil.move(str(file),folder)
            fol.rmdir()

if __name__ == "__main__":
    opening()

    folder = select_folder()
    total = 0
    for f in Path(folder):
        if f.is_file():
            total+=1
    per = permission(folder)
    count = 0
    
    if per.lower() == "y":
        count = work(folder,count)

    else:
        cnum = cause()
        cw.work(cnum)
        if cnum != 1:
            count = work(folder,count)

    issue = ending(folder,count,total)
    if issue.lower() == "n":
        issue = input("\nAre you want to Undo this whole operation?(y/n): ")

        if issue.lower() == "n":
            print("\nMaybe no problem, Thank you.\n\n")

        elif issue.lower() == "y":
            restore(folder)
            print("\nUndo All file, Successfully!\n\n")

    else:
        print("\nThank you.\n\n")