from admin_panel import *


def show_movie():
    chosen_movie = input("Enter movie: ")
    file = read_data()
    flag = False
    movie_dictionary_keys = []
    movie_dictionary_values = []

    for movie_dictionary in file:
        if movie_dictionary['name'].lower() == chosen_movie.lower():
            for key in movie_dictionary:
                movie_dictionary_keys.append(key.capitalize())

            for value in movie_dictionary.values():
                if type(value) == list:
                    new_value = ""
                    for i in range(0, len(value)):
                        new_value += str(value[i]) + " / "
                    movie_dictionary_values.append(new_value)
                else:
                    movie_dictionary_values.append(value)

            for i in range(0, len(movie_dictionary_keys)):
                print(movie_dictionary_keys[i], ":", movie_dictionary_values[i])

            flag = True

    if not flag:
        print("Try again")
        show_movie()


def add_rating():
    movie_request = input("Enter movie: ")
    dictionary = read_data()
    found = False
    for movie in dictionary:
        if movie['name'].lower() == movie_request.lower():
            new_rating = float(input("Give your rating: "))
            rating_data = movie['rating']
            full_rating = float(rating_data[0])
            rating_amount = int(rating_data[1])
            new_rating_amount = rating_amount + 1
            new_full_rating = full_rating + new_rating
            edit_row(movie['id'], 'rating', [new_full_rating, new_rating_amount])
            rating = new_full_rating / new_rating_amount

            print(f'Thanks for rating the movie! The average rating right now is {rating}')
            found = True

    if not found:
        print("Invalid rating, try again")
        add_rating()


def edit_row(id, edit_key, new_data):
    movie_dictionaries = read_data()
    file = open('IMDB_datafiles/IMDBmovies.txt', 'w')
    first = True
    for movie in movie_dictionaries:
        if first:
            keys = []
            for key in movie.keys():
                keys.append(key)
            row = '::'.join(keys)
            file.write(row + '\n')
            first = False
        if movie['id'] == id:
            movie[edit_key] = new_data
        values = []
        for value in movie.values():
            if type(value) == list:
                value = ';;'.join(str(value_item) for value_item in value)
            values.append(value)
        row = '::'.join(str(value) for value in values)
        print(row)
        file.write(row + '\n')
    file.close()


def keuzemenu():
    print("Welkom bij de Internet Movie Database! Kies uit: 1, 2, 3, 4")
    print("1. Film opvragen")
    print("2. Film raten")
    print("3. Admin login")
    print("4. Stop het programma")


#   read_data
#   key, genre: vul genre in om te filteren, laat leeg om niet te filteren.
#   returns: een list van alle dictionaries van films die door de filter zijn gekomen.


def read_data(genre='0'):
    file = open('IMDB_datafiles/IMDBmovies.txt')
    data = file.read()
    file.close()

    movies = data.splitlines()
    first = True
    movie_dictionaries = []
    for movie in movies:
        movie = movie.split('::')
        if first:
            keys = movie
            first = False
        else:
            i = 0
            movie_dictionary = {}
            for data in movie:
                if ';;' in data:
                    data = data.split(';;')
                movie_dictionary[keys[i]] = data
                i += 1
            if genre in movie_dictionary['genre']:
                movie_dictionaries.append(movie_dictionary)
            elif genre == '0':
                movie_dictionaries.append(movie_dictionary)
    return movie_dictionaries


def main():
    program_runs = True

    keuzemenu()

    while program_runs:
        i = int(input())
        #
        if i == 1:
            show_movie()
        elif i == 2:
            add_rating()
        elif i == 3:
            adminlogged = False
            adminmenu = admin_login(adminlogged)
            if adminmenu:
                print("logging succesful")
                admin_menu()
        elif i == 4:
            print("Ending program, Have a nice day!")
            program_runs = False
        else:
            raise KeyError("Input key invalid")


if __name__ == '__main__':
    main()
