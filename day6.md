Задание 1 — без запуска

Что произойдёт?

class User:
    def __init__(self, name):
        self.name = name


user = User("Alex")

print(user.name)

user.name = "Bob"

print(user.name)
1 Что выведется? - Сначала Alex, потом после изменения Bob
2 Почему user.name можно изменить напрямую? - это публичный атрибут

Задание 2 — один _

Что произойдёт?

class User:
    def __init__(self, name):
        self._name = name


user = User("Alex")

print(user._name)

Будет ли ошибка?

И главное:

Что означает _name в Python?

Ответ: Выведет Alex, ошибки не будет потому-что python технически позволяет обратиться к внутреннему атрибуту, то есть к атрибуту с _

Задание 3 — два _

Что произойдёт?

class User:
    def __init__(self, name):
        self.__name = name


user = User("Alex")

print(user.__name)

Будет ли работать?

Если нет — почему?

Ответ: Не будет работать, так как __ обозначают приваттный атрибут. Python меняет способ обращения к нему, не давая обратиться напрямую

Задание 4 — @property

Что выведет?

class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


user = User("Alex")

print(user.name)

И ответь:

почему здесь мы пишем user.name, а не user.name()?

Ответ: выведет Alex. @property позволяет обращаться к методу как к атрибуту поэтому не пишем скобки.

