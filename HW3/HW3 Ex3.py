# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def insert_num():
    num_str = input('Insert number to add to the list and press Enter or only Enter to work with list: ')
    try:
        if num_str != '':
            check = float(num_str)
    except ValueError:
        print('not a number or entered incorrectly, can not be added to list!')
        exit()
    return num_str


def make_num_list():
    num_list = []
    flag = True

    while flag:
        num_str = insert_num()
        if num_str != '':
            num_list.append(float(num_str))
        else:
            flag = False
    return num_list


def leave_float_part(float_list: list):
    result_list = []
    for num in float_list:
        result_list.append(round(num - int(num), 5))
    return result_list


def find_largest_and_smallest_elem_subtr(lst: list):
    if len(lst) == 0:
        return 0

    pos_min = 0
    pos_max = 0

    for index in range(len(lst)):
        if abs(lst[index]) < abs(lst[pos_min]):
            pos_min = index
        elif abs(lst[index]) > abs(lst[pos_max]):
            pos_max = index
    print('smallest: ' + str(lst[pos_min]) + ', largest: ' + str(lst[pos_max]))
    return abs(lst[pos_max]) - abs(lst[pos_min])


ins_list = make_num_list()
list_fl = leave_float_part(ins_list)
print(list_fl)
print('Result: ' + str(find_largest_and_smallest_elem_subtr(list_fl)))
