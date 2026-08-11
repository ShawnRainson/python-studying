def show_movies(movies):
    if is_empty(movies):
        print("List is empty!")
    else:
        number = 0
        for mov_title, mov_props in movies.items():
            number += 1
            print(f'{number} Title: {mov_title}\nYear: {mov_props["year"]}\nGenre: {mov_props["genre"]}\nRating: {mov_props["rating"]}')

def is_empty(movies):
    if not movies:
        return True
    else:
        return False

def get_count_movies(movies):
    count = 0
    for movie in movies:
        count += 1
    print(f'Count of movies: {count}')

def get_average_rating(movies):
    ratings_list = []
    count = 0
    if is_empty(movies):
        print("List is empty")
    else:
        for movie, movie_props in movies.items():
            count += 1
            ratings_list.append(movie_props["rating"])
    ratings_sum = sum(average_list)
    average = ratings_sum / count
    print(f'Average: {average}')
        