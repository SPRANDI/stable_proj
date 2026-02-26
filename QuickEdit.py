import os
import time
import sys

PUR = '\033[35m'
BLUE = '\033[34m'
RESET = '\033[0m'

BANNER = """

 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗███████╗██████╗ ██╗████████╗
 ██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██║╚══██╔══╝
 ██║   ██║██║   ██║██║██║     █████╔╝ █████╗  ██║  ██║██║   ██║   
 ██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ ██╔══╝  ██║  ██║██║   ██║   
 ╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗███████╗██████╔╝██║   ██║   
  ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   
|||               Created by >>> SPRANDI <<<                 |||

"""


lines = [line for line in BANNER.split('\n') if line.strip() != '']


max_len = max(len(line) for line in lines)
num_lines = len(lines)


thickness = 2


for row, line in enumerate(lines):
    for col, char in enumerate(line):

        target = int((row / (num_lines - 1)) * (max_len - 1)) if num_lines > 1 else 0


        if target - thickness <= col <= target + thickness:
            sys.stdout.write(BLUE + char + RESET)
        else:
            sys.stdout.write(PUR + char + RESET)
        sys.stdout.flush()
        time.sleep(0.010)
    print()


exit_flag = True
while exit_flag:
    try:
        decide = int(input(" 1. Create file\n 2. Edit file\n 3. View the file\n 4. Delete file\n 5. Exit\n >>> "))

        if decide < 1 or decide > 5:
            print("Enter a valid option")
            time.sleep(1.0)

        elif decide == 1:
            try:
                name_file = input("Name file: ")
                with open(name_file, "x", encoding='utf-8') as file:
                    info = input("File contents: ")
                    file.write(info)
                    con = input("\nThe file was created successfully\n\nPress Enter to continue\n\n")

            except FileExistsError:
                print("A file with that name already exists")
                con = input("\n\nPress Enter to continue\n\n")


        elif decide == 2:
            decide_edit = int(input(" 1. Overwrite file\n 2. Add to file\n >>> "))
            if decide_edit < 1 or decide_edit > 2:
                print(">>> Enter a valid option <<<")
                time.sleep(1.0)

            elif decide_edit == 1:

                decide_edit_file = input("Name file: ")

                if not os.path.exists(decide_edit_file):
                    print("The file was not found")
                    con = input("\n\nPress Enter to continue\n\n")
                    continue   

                overwrite = input("Overwrite file: ")
                dec = input("Overwrite file? (y/n): ")
            
                if dec == "y" or dec == "Y":
                    with open(decide_edit_file, "w", encoding='utf-8') as file:
                        file.write(overwrite)
                        con = input("\nThe file was edited successfully\n\nPress Enter to continue\n\n")

                elif dec == "n" or dec == "N":
                    continue

            elif decide_edit == 2:
                decide_edit_file = input("Name file: ")
                append = input("Add file: ")
                dec = input("Add file? (y/n): ")

                if dec == "y" or dec == "Y":
                    file = open(decide_edit_file, "a", encoding='utf-8')
                    file.write(f"\n{append}")
                    file.close()
                    con = input("\nThe file was edited successfully\n\nPress Enter to continue\n\n")

                elif dec == "n" or dec == "N":
                    continue

        elif decide == 3:
            try:
                decide_edit_file = input("Name file: ")
                with open(decide_edit_file, "r", encoding='utf-8') as file:
                    print(file.read())
                    con = input("\n\nPress Enter to continue\n\n")

            except FileNotFoundError:
                print("The file was not found ")
                con = input("\n\nPress Enter to continue\n\n")

        elif decide == 4:
            try:
                decide_del_file = input("Name file: ")
                decc = input("Delete file? (y/n): ")
                if decc == "y" or decc == "Y":
                    os.remove(decide_del_file)
                    print("\nThe file was deleted successfully")
                    con = input("\n\nPress Enter to continue\n\n")

                elif decc == "n" or decc == "N":
                    print("The file was not deleted")
                    con = input("\nPress Enter to continue\n\n")
            
            except FileNotFoundError:
                print("The file was not found ")
                con = input("\n\nPress Enter to continue\n\n")

        elif decide == 5:
            exit_flag = False
        
    except ValueError:
        print("Enter a number ")
        con = input("\n\nPress Enter to continue\n\n")
