# Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def find_odd_index_sum(lst: list):
    sum = 0
    for i in range(1, (len(lst)), 2):
        sum += int(lst[i])
    return sum


def insert_and_check_list():
    inserted_list = (input('Enter list of integers separated by commas and press Enter: '))
    num_list = inserted_list.split(',')
    check = 0
    try:
        for i in num_list:
            check += int(i)
    except:
        print(inserted_list)
        print('The list contains non-numbers!')
        exit()
    return num_list


lst = insert_and_check_list()
print(lst)
print('Sum of list elements in odd positions: ' + str(find_odd_index_sum(lst)))

