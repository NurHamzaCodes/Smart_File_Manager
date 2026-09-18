from pathlib import Path
import shutil

def work(cnum):
    match cnum:
        case 1:
          print("\nAll Right, No File Moved!")
        case 2:
          cata = input("\nType which category folder's name you want to change: ")
          creta = input("Give the changing name: ")

        case 3:
            pass
        case 4:
            pass