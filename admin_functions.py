def add_movie():
    file = open("IMDB_datafiles/IMDBmovies.txt", "a")

    title = input("1/9 Title: ")
    rel_date = input("2/9 Release date: ")
    prod = input("3/9 producer: ")
    sales = input("4/9 sales: ")
    nomination = input("5/9 nominations: ")
    distri = input("6/9 distributors: ")
    genre = input("7/9 genre: ")
    sub_genre = input("8/9 sub-genre: ")
    content_type = input("9/9 type (film or movie): ")
    rating_yn = input("Does the movie alread have a rating?: ").lower()

    if rating_yn == "y":
        rating_avg = input("Please Enter the avarage rating: ")
        rating_freq = input("Please Enter the total number of ratings: ")

        data = (f"\n"
                f"{title}::"
                f"{rel_date}::"
                f"{prod}::"
                f"{sales}::"
                f"{nomination}::"
                f"{distri}::"
                f"{genre}::"
                f"{sub_genre};;"
                f"{content_type}::"
                f"{rating_avg};;"
                f"{rating_freq}::"
                f"null_rewards")
    elif rating_yn == "n":

        data = (f"\n"
                f"{title}::"
                f"{rel_date}::"
                f"{prod}::"
                f"{sales}::"
                f"{nomination}::"
                f"{distri}::"
                f"{genre}::"
                f"{sub_genre};;"
                f"{content_type}::"
                f"null_rating::"
                f"null_rewards")
    else:
        raise KeyError("Invalid key, NO DOCUMENT CHANGES HAVE BEEN MADE")

    file.writelines(data)
    file.close()
    # print(f"{title} {rel_date} {prod} {sales} {nomination} {distri} {genre} {content_type}")


def delete_movie():
    movie_writing_dict = {}
    movie_writing_list = ()

    movie_to_delete_output = input("(Q to cancel) What movie do you want to delete?: ")
    movie_to_delete = movie_to_delete_output.lower().replace(" ", "")

    if movie_to_delete == "q":
        print("cancelling deletion, no changes have been made")
        return 0

    else:
        file = open("IMDB_datafiles/IMDBmovies.txt", "r")
        movies_lib = file.readlines()

        for movie in range(len(movies_lib)):
            movie_name = movies_lib[movie].split("::")[0]

            if movie_name == movie_to_delete:
                print(f"do you want to delete '{movie_to_delete_output}'? Y/N")
                delete_answer = input().lower()

                if delete_answer == "y":
                    print("deleting movie...")

                    for movies in range(len(movies_lib)):

                        if movie_to_delete == movies_lib[movies].split("::")[0]:
                            print(f"will not write {movie_name}")
                        else:
                            #file = open("IMDB_datafiles/IMDBmovies.txt", "w")
                            print(movies_lib[movies].split("::"))

                elif delete_answer == "n":
                    print("cancelling deletion, no changes have been made")

                else:
                    raise KeyError("Key invalid, please restart to continue")


delete_movie()
