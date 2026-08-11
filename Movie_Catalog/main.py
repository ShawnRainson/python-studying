import movies as m
import helpers as h

movies_list = {}
def start():
    while True:
        try:
            print("MENU:\n" \
            "1. Add movie\n" \
            "2. Show movie list\n" \
            "3. Remove movie\n" \
            "4. Exit")
        
            choice = int(input("Choose menu option (1-4): "))
        
            if choice == 1:
                m.add_movie(movies_list)
            elif choice == 2:
                h.show_movies(movies_list)
            elif choice == 3:
                m.remove_movie(movies_list)
            elif choice == 4:
                print("Bye-bye!")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Invalid value!")

start()
    

