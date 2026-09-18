from pathlib import Path
import shutil
import main

def work(cnum):
    match cnum:
        case 1:
          print("\nAll Right, No File Moved!")
        case 2:
          cata = input("\nType which category folder's name you want to change: ")
          if cata in main.category.values():
              creta = input("Give the new name of folder: ")
              for key in main.category.keys():
                  if main.category[key] == cata:
                      main.category[key] = creta

          else:
              print("This ")


        case 3:
            pass
        case 4:
            pass