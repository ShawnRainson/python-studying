def show_movies(movies):
    number = 0
    for mov_title, mov_props in movies.items():
        number += 1
        print(f'{number} Title: {mov_title}\nYear: {mov_props["year"]}\nGenre: {mov_props["genre"]}\nRating: {mov_props["rating"]}')
        