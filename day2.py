#Практика — пишешь код сам
#Задача 4 — сумма чисел
def my_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(my_sum(1, 2, 3))
print(my_sum(5, 10, 15, 20))

#Задача 5 — карточка пользователя

def user_card(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_card(name="Alex", age=20, city="Moscow")

#Мини-челлендж (со звёздочкой)

def welcome(message, *names):
    for name in names:
        print(f"{message}, {name}!")

welcome("Добро пожаловать", "Анна", "Иван", "Олег")

#адание 9 — пишешь сам

def calculate(a, b, operation):
    if operation == "add":
        print(a + b)
    elif operation == "subtract":
        print(a - b)
    elif operation == "multiply":
        print(a * b)
    elif operation == "divide":
        print(a // b)
    else:
        print("Error: Unknown operation!")

add_op = [10, 5, "add"]
sub_op = [10, 5, "subtract"]
mul_op = [10, 5, "multiply"]
div_op = [10, 5, "divide"]
err_op = (10, 5, "error")

calculate(*add_op)
calculate(*sub_op)
calculate(*mul_op)
calculate(*div_op)
calculate(*err_op)

#Задание 10 — соединяем всё

def calculate_all(operation, *numbers):
    if operation == "add":
        result = 0
        for i in numbers:
            result += i
    elif operation == "substract":
        result = numbers[0]
        for i in numbers[1:]:
            result -= i
    elif operation == "multiply":
        result = 1
        for i in numbers:
            result *= i
    elif operation == "divide":
        result = numbers[0]
        for i in numbers[1:]:
            result /= i


    print(f"Result: {result}")

add_op = ["add", 1, 2, 3, 4]
sub_op = ["substract", 1, 2, 3, 4]
mul_op = ["multiply", 1, 2, 3, 4]
div_op = ["divide", 1, 2, 3, 4]

calculate_all(*add_op)
calculate_all(*sub_op)
calculate_all(*mul_op)
calculate_all(*div_op)