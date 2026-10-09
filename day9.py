#Задание 5. Базовый класс и наследник
#Задание 6. Используем super()
#Задание 9. Специальные методы
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def describe(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"

    def speak(self):
        return "Woof!"

    def introduce(self):
        return f"My name is {self.name}"

    def describe(self):
        return super().describe() + ", " + f"Breed: {self.breed}"

dog = Dog("Rex", "Husky")

print(dog.speak())
print(dog.introduce())
print(dog.describe())
print(dog)

#Задание 6. Используем super()
class EmailNotification:
    def send(self):
        return "Sending email."

class SMSNotification:
    def send(self):
        return "Sending SMS"

notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:
    print(notification.send())

#Задание 8. Инкапсуляция и @property
class User:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return f"User age: {self.__age}"

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self.__age = value

user = User(25)
print(user.age)

user.age = -10

        


