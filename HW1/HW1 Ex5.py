# Задача 5 VERY HARD SORT необязательная
#
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
#
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10
import random


def generate_multi_list(rows: int, cols: int):
    multi_list = [[random.randint(1, 100) for col in range(0, cols)] for row in range(0, rows)]
    return multi_list


def print_multi_list(multi_dim_list: list):
    for line in multi_dim_list:
        print(line)


def multi_list_to_list(multi_list: list):
    one_dim_list = []
    for line in multi_list:
        for num in line:
            one_dim_list.append(num)
    return one_dim_list


def list_sort(one_dim_list: list):
    for index in range(len(one_dim_list)):
        min_pos = index
        for j in range(index + 1, len(one_dim_list)):
            if one_dim_list[j] < one_dim_list[min_pos]:
                min_pos = j
        one_dim_list[min_pos], one_dim_list[index] = one_dim_list[index], one_dim_list[min_pos]
    return one_dim_list


def list_to_multi_list(one_dim_list: list, multi_list: list):
    counter = 0
    for line in range(len(multi_list)):
        for num in range(len(multi_list[line])):
            multi_list[line][num] = one_dim_list[counter]
            counter += 1
    return multi_list


try:
    row = int(input('Please insert rows number: '))
    col = int(input('Please insert columns number: '))

    generated_list = generate_multi_list(row, col)
    print_multi_list(generated_list)
    one_line_list = multi_list_to_list(generated_list)
    sorted_list = list_sort(one_line_list)
    print('---Sorted----')
    print_multi_list(list_to_multi_list(sorted_list, generated_list))

except:
    print('Not a number!')
