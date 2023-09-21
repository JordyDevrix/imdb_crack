login = False


def admin_login(entered_username):
    global login
    file = open("IMDB_datafiles/admin_passwords.txt", "r")
    username_lines = file.readlines()
    for line in range(len(username_lines)):
        username = username_lines[line].split("::")[0].replace("\n", "")
        if username == entered_username:
            enter_password = input("Enter password: ")
            password = username_lines[line].split("::")[1].replace("\n", "")
            if password == enter_password:
                login = True
                return "Logging in..."
            else:
                login = False
                return "Password invalid, please try again"
        elif line + 1 == len(username_lines):
            return "Username not found"


enter_username = input("Enter username: ")
print(admin_login(enter_username.replace(" ", "").lower()))

if login:
    print("login succesfull")