# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def insert_num():
    num_str = input('Insert number to add to the list and press Enter or only Enter to work with list: ')
    try:
        if num_str != '':
            check = int(num_str)
    except ValueError:
        print('Not a number or entered incorrectly, can not be added to list!')
        exit()
    return num_str


def make_num_set():
    num_set = set()
    result_list = []
    flag = True

    while flag:
        num_str = insert_num()
        if num_str != '':
            if int(num_str) not in num_set:
                num_set.add(int(num_str))
                result_list.append(int(num_str))
        else:
            flag = False
    return result_list


print('Non-repeating elements are: ' + str(make_num_set()) + ' in insertion order.')
