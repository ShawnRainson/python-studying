
def add_movie(movie):
    properties = {}
    movie_title = input("Enter movie title: ")
    movie_year = int(input("Enter movie year of realise: "))
    properties["year"] = movie_year
    movie_genre = input("Enter movie genre: ")
    properties["genre"] = movie_genre
    movie_rating = float(input("Enter movie rating: "))
    properties["rating"] = movie_rating
    movie[movie_title] = properties
    print("New movie was added!")

def remove_movie(movies):
    movie_title = input("Enter movie title for removing: ")
    del movies[movie_title]
    print("Movie data was removed!")


