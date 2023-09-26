from admin_panel import *


def show_movie():
    chosen_movie = input("Enter movie: ")
    file = read_data()
    flag = False

    for movie_dictionary in file:
        movie_dictionary_keys = []
        movie_dictionary_values = []
        if movie_dictionary['name'].lower() == chosen_movie.lower():
            for key in movie_dictionary:
                movie_dictionary_keys.append(key.capitalize())

            for value in movie_dictionary.values():
                if type(value) == list:
                    if value[1].isnumeric():
                        #   see if value is numeric, if so: value is a rating else: value is a type (movie or series)
                        if int(value[1]) == 0:
                            #   see if rating is 0, if so it will append there is no rating yet
                            rating = "No rating yet"
                            movie_dictionary_values.append(rating)
                        else:
                            #   rating has been found therefore it will append the rating to the dictionary
                            rating = float(value[0]) / int(value[1])
                            movie_dictionary_values.append(rating)
                    else:
                        new_value = " / ".join(value)
                        movie_dictionary_values.append(new_value)
                else:
                    movie_dictionary_values.append(value)

            for i in range(0, len(movie_dictionary_keys)):
                if len(movie_dictionary_keys) == i + 1:
                    print(f"{movie_dictionary_keys[i]} : {movie_dictionary_values[i]} \n")
                else:
                    print(f"{movie_dictionary_keys[i]} : {movie_dictionary_values[i]}")
            flag = True
    choice_menu()

    if not flag:
        print("Try again")
        show_movie()


def add_rating():
    movie_request = input("(Q to cancel) Enter movie: ")
    dictionary = read_data()
    found = False
    for movie in dictionary:
        if movie_request == "q" or movie_request == "Q":
            print("Cancelling add rating. No changes have been made\n")
            choice_menu()
            return 0
        elif movie['name'].lower() == movie_request.lower():
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


def edit_row(id_m, edit_key, new_data):
    movie_dictionaries = read_data()
    file = open('IMDB_datafiles/IMDBmovies.txt', 'w')
    first = True
    counter = 0

    for movie in movie_dictionaries:
        counter = counter + 1
        if first:
            keys = []
            for key in movie.keys():
                keys.append(key)
            row = '::'.join(keys)
            file.write(row + '\n')
            first = False
        if movie['id'] == id_m:
            movie[edit_key] = new_data
        values = []
        for value in movie.values():
            if type(value) == list:
                value = ';;'.join(str(value_item) for value_item in value)
            values.append(value)
        row = '::'.join(str(value) for value in values)
        #   print(row)
        #   print(len(movie_dictionaries))
        #   print(counter)
        if counter == len(movie_dictionaries):
            file.write(row)
        else:
            file.write(row + '\n')
    file.close()


def choice_menu():
    print("[1] Film opvragen")
    print("[2] Film raten")
    print("[3] Admin login")
    print("[4] Stop het programma")


def on_start():
    print("Welkom bij de Internet Movie Database! Kies uit: 1, 2, 3, 4")


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

    on_start()
    choice_menu()

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
                print("logging succesful\n")
                admin_menu()
        elif i == 4:
            print("Ending program, Have a nice day!")
            program_runs = False
        else:
            raise KeyError("Input key invalid")


if __name__ == '__main__':
    main()
