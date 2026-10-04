#Задание 4 — __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"

book = Book("1984", "George Orwell")
print(book)

#Задание 5 — __len__
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __str__(self):
        return f"{self.songs}"
    
    def __len__(self):
        return len(self.songs)

    def __eq__(self, other):
        return self.songs == other.songs

    def __getitem__(self, index):
        return self.songs[index]
        
        

playlist = Playlist(["Numb", "Faint", "In The End"])
print(playlist)
print(len(playlist))
print(playlist[0])
playlist2 = Playlist(["Numb", "Faint", "In The End"])
print(playlist == playlist2)

#⭐ Задание 6 — __eq__

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

user1 = User("Alex", 25)
user2 = User("Alex", 25)
user3 = User("Bob", 30)

print(user1 == user2)
print(user1 == user3)

#🔥 Бонус — __getitem__

class Team:
    def __init__(self):
        self.players = []

    def __getitem__(self, index):
        return self.players[index]

team = Team()
team.players.append("Alex")
team.players.append("Bob")
team.players.append("Mike")

print(team[0])
print(team[2])