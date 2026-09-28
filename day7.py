#Задание 4
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        return age >= 18

user = User.from_string("Alex, 25")
print(user.name)
print(user.age)

#Задание 5 — staticmethod
print(User.is_adult(25))
print(User.is_adult(15))

        