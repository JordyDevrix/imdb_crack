from admin_panel import *


def new_rating():
    user_movie = input("Enter movie: ")
    dictionary = read_data()

    for movie in dictionary:
        if movie['name'] == user_movie.capitalize():
            user_rating = float(input("Give your rating: "))
            info = movie['rating']
            average_rating = float(info[0])
            count = int(info[1])
            count += 1

            rating = (average_rating + user_rating)/count

            return f'Thanks for rating the movie! The average rating right now is {rating}'

        else:
            return "Invalid rating, try again"


def keuzemenu():
    print("Welkom bij de Internet Movie Database! Kies uit: 1, 2, 3, 4")
    print("1. Film opvragen")
    print("2. Film raten")
    print("3. Admin login")
    print("4. Stop het programma")

#   read_data
#   key, genre: vul genre in om te filteren, laat leeg om niet te filteren.
#   returns: een list van alle dictionaries van films die door de filter zijn gekomen.


def read_data(genre = 0):
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
            elif genre == 0:
                movie_dictionaries.append(movie_dictionary)

    return movie_dictionaries


def main():
    program_runs = True

    keuzemenu()

    while program_runs:
        i = int(input())

        if i == 1:
            read_data()
            print(read_data())
        elif i == 2:
            rating = new_rating()
            print(rating)
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
