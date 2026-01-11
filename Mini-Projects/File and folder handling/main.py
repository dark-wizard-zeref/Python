from pathlib import Path
import shutil

def create_folder():
    try:
        name = input("Enter what you want to name this folder: ")
        p = Path(name)
        p.mkdir()
        print("folder created successfully...")
    except Exception as err:
        print(f"Sorry an error showed up as {err}")


def read_file_folder():
    p = Path(".")
    items = list(p.rglob('*'))
    for i,v in enumerate(items):
        if v.is_dir():
            print(f"{i+1} : [DIR] {v}")
        else:
            print(f"{i+1} : [FILE] {v}")


def update_folder():
    try:
        read_file_folder()
        old_name = input("Enter name of folder you want to update: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input(f"Enter name which you want to rename {old_name} with: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your Folder name has been updated successfully...")
        else:
            print("Sorry this Folder does not exist...")
    except Exception as err:
        print(f"An error occured as {err}")


def delete_folder():
    try:
        read_file_folder()
        name = input("Enter name of folder you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)     # No need to worry about non empty directories
            print("Folder deleted successfully...")
        else:
            print("No such folder exists...")
    except Exception as err:
        print(f"There was an error as {err}")


def create_file():
    try:
        read_file_folder()
        name = input("Enter file path and name: ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("Write something in your new file: ")
                fs.write(data)
                print("File created successfully...")
        else:
            print("Sorry this file name already exist")
    except Exception as err:
        print(f"An error occured as {err}")


def read_file():
    try:
        read_file_folder()
        name = input("Name the file which you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                content = fs.read()
                print("Your file content is: \n",content)
        else:
            print("Sorry no such file exist...")
    except Exception as err:
        print(f"An exception occured as {err}")


def update_file():
    try:
        read_file_folder()
        name = input("Enter file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Options: \n\t1. for renaming the file\n\t" \
            "2. for appending something in file\n\t3. for overwriting file content")
            choice = int(input("Tell your choice: "))
            if choice == 1:
                new_name = input("Enter name you want to rename the file with:")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name has been changed successfully...")
                else:
                    print("Sorry this name already exists...")
            if choice == 2:
                with open(p,'a') as fs:
                    data = input("Write content you need to add in the file: ")
                    fs.write(" "+data)
                print("Your file has been Updated...")
            if choice == 3:
                with open(p,'w') as fs:
                    data = input("Write content to overwrite in your file: ")
                    fs.write(data)
                print("Your file has been Changed...")
    except Exception as err:
        print(f"An error occured as {err}")


def delete_file():
    try:
        read_file_folder()
        name = input("File you want to delete with its extension: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File Deleted successfully...")
        else:
            print("Sorry no such file exists...")
    except Exception as err:
        print(f"An error occured as {err}")


def main_menu():
    print("Options:\n\t0. Exit\n\t1. Create a folder\n\t2. Read files and folders\n\t" \
    "3. Update the folder\n\t4. Delete the folder \n\t5. Create a file\n\t" \
    "6. Read a file\n\t7. Update a file\n\t8. Delete a file")


def user_choice():
    choice = int(input("\tPlease choose your option: "))
    return choice


def operations(choice):
    if choice == 0:
        exit()
    if choice == 1:
        create_folder()

    if choice == 2:
        read_file_folder()

    if choice == 3:
        update_folder()

    if choice == 4:
        delete_folder()
    
    if choice == 5:
        create_file()
    
    if choice == 6:
        read_file()

    if choice == 7:
        update_file()
    
    if choice == 8:
        delete_file()


while True:
        main_menu()
        choice = user_choice()
        operations(choice)