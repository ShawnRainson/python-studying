def add_item(items):
    res = items.copy()
    res.append(100)
    return res

numbers = [1, 2, 3]
result = add_item(numbers)
print(numbers)
print(result)

def add_unique(items, value):
    res = items.copy()
    if value not in res:
        res.append(value)
    return res

numbers = [1, 2, 3]
result1 = add_unique(numbers, 4)
result2 = add_unique(numbers, 3)
print(result1)
print(result2)
