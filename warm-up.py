numbers = [4, 7, 2, 7, 9, 4, 7, 2]
number_dict = {}

for num in numbers:
    if num not in number_dict:
        number_dict[num] = 1
    else:
        number_dict[num] += 1
print(number_dict)