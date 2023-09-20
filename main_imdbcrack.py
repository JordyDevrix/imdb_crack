def keuzemenu():
    print("Welkom bij de Internet Movie Database! Kies uit: 1, 2, 3, 4, 5, 6")
    print("1. Film opvragen")
    print("2. Film raten")
    print("3. Beschrijving opvragen")
    print("4. Film toevoegen | Admin")
    print("5. Serie toevoegen | Admin")
    print("6. Film/serie verwijderen | Admin")
    print("7. Stop het programma")


def main():
    program_runs = True

    keuzemenu()

    while program_runs:
        i = input()


if __name__ == '__main__':
    main()
