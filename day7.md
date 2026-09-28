Задание 1

Что произойдёт?

class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello {self.name}"

user = User("Alex")

print(user.hello())

Вопросы:

1 Что выведется? - Hello Alex
2 Что такое self внутри hello()? - по сути то что мы передаём
3 Почему здесь нужен self? - потому-что это обычный метод относящийся к объекту

Задание 2 — classmethod
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

user1 = User("Alex")
user2 = User("Bob")
user3 = User("John")

print(User.get_count())

Ответь:

1 Что выведется? - 3
2 Что такое cls? - что-то вроде self, но относится к классу
3 Что будет находиться в cls во время выполнения get_count()? - count

Задание 3 — главное отличие

Что произойдёт здесь?

class User:
    count = 0

    @classmethod
    def show_count(cls):
        return cls.count

    @staticmethod
    def say_hello():
        return "Hello!"

print(User.show_count()) - 0
print(User.say_hello()) - Hello

Почему show_count() получает cls, а say_hello() — нет?
Ответ: потому-что первый это метод класса, а второй статический метод, ему не нужен ни self ни cls

🔥 Финальная проверка Дня 7

Без запуска кода:

class Animal:

    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    @classmethod
    def how_many(cls):
        return cls.count

    @staticmethod
    def info():
        return "Animals are living beings"


dog = Animal("Rex")
cat = Animal("Murzik")

print(dog.name)
print(Animal.how_many())
print(Animal.info())

Ответь на три вопроса:

1 Что выведет каждая из трёх print? - Rex, 2, Animals are living beings
2 Что будет находиться в self при создании dog? - dog
3 Что будет находиться в cls внутри how_many()? - Animal