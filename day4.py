#Задание 5 — безопасное деление
def divide(a, b):
    return a / b

try:
    result = divide(4, 2)
except ZeroDivisionError:
    print("You cant divide on zero.")
else:
    print("Result: ", result)

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("You cant divide on zero.")
else:
    print("Result: ", result)


#Задание 6 — проверка возраста

def validate_age(age):
    if age < 0:
        raise ValueError("Age cant be negative!")
    elif age > 150:
        raise ValueError("Age cant be more than 150 years.")
    else:
        return f'Age: {age}'

result1 = validate_age(21)
result2 = validate_age(-21)
result3 = validate_age(210)
print(result1)
print(result2)
print(result3)



#Задание 7 — комбинируем
def get_number():
    value = input("Enter number: ")
    try:
        num = int(value)
    except ValueError:
        print("This is not a number!")
    else:
        print(f'Number: {num}')

get_number()

#Задание 8 — сенсейский челлендж

def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Error: Amount cant be negative!")
    elif amount > balance:
        raise ValueError("Error: Amount cant be more than balance!")
    else:
        new_bal = balance - amount
        return f'Your balance now: {new_bal}'