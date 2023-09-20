def keuzemenu():
    print("Welkom bij de Internet Movie Database! Kies uit: 1, 2, 3, 4, 5, 6")
    print("1. Film opvragen")
    print("2. Film raten")
    print("3. Beschrijving opvragen")
    print("4. Film toevoegen | Admin")
    print("5. Serie toevoegen | Admin")
    print("6. Film/serie verwijderen | Admin")
    print("7. Stop het programma")

def read_data(genre = 0):
    file =  open('IMDB_datafiles/IMDBmovies.txt')
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
    print(movie_dictionaries)

def main():
    read_data('sciencefiction')
    # program_runs = True

    # keuzemenu()

    # while program_runs:
    #     i = input()


if __name__ == '__main__':
    main()
