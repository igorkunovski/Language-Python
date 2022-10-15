# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def insert_num():
    num_str = input('Insert number to add to the list and press Enter or only Enter to work with list: ')
    try:
        if num_str != '':
            check = int(num_str)
    except ValueError:
        print('not a number, can not be added to list!')
        exit()
    return num_str


def make_num_list():
    num_list = []
    flag = True

    while flag:
        num_str = insert_num()
        if num_str != '':
            num_list.append(int(num_str))
        else:
            flag = False
    return num_list


def multiplication(num_lst: list):
    result_list = []
    half_len = int(len(num_lst) / 2 + len(num_lst) % 2)
    for index in range(half_len):
        result_list.append(num_lst[index] * num_lst[-1 - index])
    return result_list


new_list = make_num_list()
print(new_list)
result_lst = multiplication(new_list)
print(result_lst)
