#Задание 5 — защищённый баланс and 🔥 Задание 6 — Property
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)
print(account.balance)

#⭐ Задание 7 — самое важное

class User:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

user = User(25)

print(user.age)

user.age = -10