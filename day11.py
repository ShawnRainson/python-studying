from copy import deepcopy
#Задание 6. Уникальные элементы
def unique_items(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    print(new_list)

unique_items([3, 1, 3, 2, 1, 4])

#Задание 7. Список покупок
def process_shopping_list(items):
    list_copy = items.copy()
    list_copy.remove("milk")
    list_copy.sort()
    return list_copy

items = ["bread", "milk", "apple", "milk"]
result = process_shopping_list(items)

print(result)
print(items)

#Задание 8. Безопасное копирование
def copy_matrix(matrix):
    new_matrix = deepcopy(matrix)
    return new_matrix

matrix = [[1, 2], [3, 4]]
copied = copy_matrix(matrix)

copied[0].append(99)

print(matrix) 
print(copied)

#⭐ Мини-челлендж сенсея

def update_inventory(inventory):
    invent_copy = deepcopy(inventory)
    invent_copy[1].append("monitor")
    invent_copy[0].remove("phone")
    return invent_copy

inventory = [
    ["laptop", "phone"],
    ["keyboard", "mouse"],
    ["laptop", "tablet"]
]

process_result = update_inventory(inventory)
print(process_result)