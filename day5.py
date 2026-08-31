#Задание 5 — User
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'My name is {self.name}, I am {self.age} years old.')

user = User("Alex", 25)
print(user.name)
print(user.age)


#Задание 6 — метод

user.introduce()

#Задание 7 — изменяем состояние объекта
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print(account.balance)


#Задание 8 — наследование 

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()
