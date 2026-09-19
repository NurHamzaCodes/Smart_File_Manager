import variable as va

def work(cnum):
    match cnum:
        case 1:
          print("\nAll Right, No File Moved!")
        case 2:
          cata = input("\nType which category folder's name you want to change: ")
          if cata in va.category.values():
              creta = input("Give the new name of folder: ")
              for key in va.category.keys():
                  if va.category[key] == cata:
                      va.category[key] = creta
            
          else:
              print("There is no name in categories.")
              work(cnum=2)

        case 3:
            extention = input("\nGive the extention of files: ").lower()
            if not extention.startswith("."):
                extention = "."+extention

            name = input(f"Give the folder name for {extention} files: ")
            va.category[extention] = name