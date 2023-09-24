from admin_functions import add_movie


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
            print("Username not found")
            return login


def admin_menu():
    print("[1] add a movie.\n[2] option two.\n[3] option three.")
    option = int(input(""))

    if option == 1:
        add_movie()
    elif option == 2:
        print("Not finished yet")
    elif option == 3:
        print("Not finished yet")
    else:
        raise KeyError("Key invalid, please restart to continue")

