Задание 1

Что произойдёт?

try:
    number = int("abc")
    print(number)

except ValueError:
    print("Ошибка преобразования")

Что выведется и почему?

Ответ: Выведет ошибку "Ошибка преобразования", так как в блоке try идёт попытка преобразовать строку "abc" в целове число int

Задание 2

Что выведет программа?

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Ошибка")

else:
    print("Успешно:", result)

finally:
    print("Конец")

Напиши порядок вывода строк.
Ответ:
1 Успешно: 5
2 Конец

Задание 3

Что произойдёт?

try:
    numbers = [1, 2, 3]
    print(numbers[10])

except ValueError:
    print("ValueError")

except IndexError:
    print("IndexError")

Какой except сработает и почему?

Ответ: Сработает IndexError, так как в try идйт попытка обратиться к индексу 10, хотя в списку всего 3 элемента.

Задание 4

Что произойдёт?

try:
    number = int("abc")

except Exception:
    print("Exception")

except ValueError:
    print("ValueError")

Как думаешь, какой except сработает?

И почему порядок except здесь имеет значение?

Ответ: Не уверен, но мне кажется сработает Exception, и вот почему: 
1 Python попробует обработать код из try - не получится
2 Он пойдёт смотреть except и первым найдёт Exception
3 Так как Exception работает на всех ошибках, сработает именно этот блок.

