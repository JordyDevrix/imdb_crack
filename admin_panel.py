from admin_functions import *


def admin_login(login):
    entered_username = input("Enter username: ")
    file = open("IMDB_datafiles/admin_passwords.txt", "r")
    username_lines = file.readlines()
    for line in range(len(username_lines)):
        username = username_lines[line].split("::")[0].replace("\n", "")
        if username == entered_username:
            enter_password = input("Enter password: ")
            password = username_lines[line].split("::")[1].replace("\n", "")
            if password == enter_password:
                login = True
                print("Logging in...")
                return login
            else:
                login = False
                print("Password invalid, please try again")
                return login
        elif line + 1 == len(username_lines):
            login = False
            print("Username not found, try again")
            return login


def admin_menu():
    print("[1] add a movie.\n[2] delete a movie.\n[3] return to main menu.")
    option = int(input(""))

    if option == 1:
        add_movie()
        admin_menu()
    elif option == 2:
        delete_movie()
        admin_menu()
    elif option == 3:
        print("returning...\n")
        print("[1] Film opvragen")
        print("[2] Film raten")
        print("[3] Admin login")
        print("[4] Stop het programma")
        return 0
    else:
        raise KeyError("Key invalid, please restart to continue")

