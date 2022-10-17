# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб
# количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы
# массива, причем чтобы каждый гарантированно переместился на другое место и
# выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И
# далее в конце опять вывести на экран как таблицу.

from random import *

try:
    rows = int(input('Please insert rows number: '))
    cols = int(input('Please insert columns number: '))
except ValueError:
    print('Incorrect int value!')
    exit()
index_list = []
iterations = int(rows * cols / 2) + (rows * cols) % 2


def generate_index_list():
    for i in range(rows * cols):
        index_list.append(i)
    return index_list


def generate_multi_list():
    multi_list = [[choice(range(100)) for col in range(0, cols)] for row in range(0, rows)]
    generate_index_list()
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


def list_to_multi_list(one_dim_list: list, multi_list: list):
    counter = 0
    for line in range(len(multi_list)):
        for num in range(len(multi_list[line])):
            multi_list[line][num] = one_dim_list[counter]
            counter += 1
    return multi_list


def shuffle_list(lst: list):

    for i in range(iterations):
        rand_index = choice(index_list[iterations:])
        if i != rand_index:
            lst[i], lst[rand_index] = lst[rand_index], lst[i]
            index_list.remove(rand_index)
    return lst


new_list = generate_multi_list()
print_multi_list(new_list)
one_d_list = multi_list_to_list(new_list)
shuffle_list(one_d_list)
inserted_list = list_to_multi_list(one_d_list, new_list)
print('--------------------')
print_multi_list(inserted_list)


