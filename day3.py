#Задача 5 — счётчик

def make_counter():
    x = 0

    def inner():
        nonlocal x
        x += 1
        return x

    return inner

counter = make_counter()

print(counter())
print(counter())
print(counter())

#Задача 6 — фабрика приветствий

def make_greeting(prefix):

    def name_greeting(name):
        return f"{prefix}, {name}!"
    return name_greeting

hello = make_greeting("Привет")
goodbye = make_greeting("Пока")

print(hello("Иван"))
print(goodbye("Иван"))

#Мини-челлендж

def make_power(power):

    def power_number(number):
        return number ** power
    return power_number
square = make_power(2)
cube = make_power(3)

print(square(5))
print(cube(5))