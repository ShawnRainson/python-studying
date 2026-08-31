Задание 1 — без запуска

Что выведет?

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}: Woof!")


dog1 = Dog("Rex")
dog2 = Dog("Max")

dog1.bark()
dog2.bark()

Напиши вывод и объясни, почему имена разные.

Ответ: Выведет Rex: Woof! Max: Woof!, имена разные потому-что разные объекты, с разными заданными именами.

Задание 2

Что здесь означает self?

class User:
    def __init__(self, name):
        self.name = name

Объясни своими словами, что произойдёт при:

user = User("Alex")

Ответ: Точно объяснить что такое self не могу, но при user = User("Alex") теперь мы можем обращаться к методам через user.

Задание 3

Что выведет?

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


counter = Counter()

counter.increment()
counter.increment()

print(counter.value)

Почему значение стало именно таким?

Ответ: Выведет 2, потому-что метод increment увеличивает значение на 1. value в начале равен 0, increment вызван 2 раза

Задание 4 — класс или объект?

Для каждого названия скажи, что это:

class Car:
    pass

car1 = Car()
car2 = Car()
Car — Класс
car1 — Объект
car2 — Объект
car1 is car2 — True или False?
Ответ: Не уверен, но наверное false, так как это разные объекты.
