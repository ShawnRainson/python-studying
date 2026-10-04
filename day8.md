Задание 1

Что выведет:

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"


user = User("Alex")

print(user) - User: Alex

И почему print(user) вызывает __str__? - Потому что по сути идёт к нему обращение self.__str__(user)

Задание 2

Что произойдёт?

class Cart:
    def __init__(self):
        self.items = ["Apple", "Milk"]

    def __len__(self):
        return len(self.items)


cart = Cart()

print(len(cart)) - 2

Что будет находиться в self внутри __len__? - список

Задание 3

Без запуска:

class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


user1 = User("Alex")
user2 = User("Alex")
user3 = User("Bob")

print(user1 == user2) - True - одинаковые значени
print(user1 == user3) - False - разные значения

Что выведется и почему?