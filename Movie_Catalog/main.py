from helpers import show_movies, get_count_movies
from movies import add_movie, remove_movie, get_average_rating

movies_list = {}
def start():
    while True:
        try:
            print("MENU:\n" \
            "1. Add movie\n" \
            "2. Show movie list\n" \
            "3. Remove movie\n" \
            "4. Count of movies\n" \
            "5. Ratings average\n" \
            "6. Exit")
        
            choice = int(input("Choose menu option (1-6): "))
        
            if choice == 1:
                add_movie(movies_list)
            elif choice == 2:
                show_movies(movies_list)
            elif choice == 3:
                remove_movie(movies_list)
            elif choice == 4:
                get_count_movies(movies_list)
            elif choice == 5:
                get_average_rating(movies_list)
            elif choice == 6:
                print("Bye-bye!")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Invalid value!")

start()
    

