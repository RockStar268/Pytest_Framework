def movies_list():
    movies = []
    movies.append("Pirates of the Carribean")
    movies.append("Pokèmon")
    movies.append("Fast and Furious")
    movies.append("Transformers")
    movies.append("Maze Runner")

    print("Validation of newly created list of movies: " + str(movies))
    print("============")

    for each_movie in movies:
        print(each_movie)
    print("============")

    for each_movie in movies[1:3]:
        print("method 1 " + each_movie)
    print("============")
    print(movies[1:3])
    print("============")
    print(str(movies[-2]))
    print("============")

movies_list()

