# Задача 5 необязательная Дан список чисел. Создайте список, в который попадают
# числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

def find_list(min_num: int, lst: list):
    temp_lst = [min_num]
    while min_num + 1 in lst:
        temp_lst.append(min_num + 1)
        min_num += 1
    return temp_lst


def get_longest(lst: list):
    longest = lst[0]
    for line in lst:
        if len(line) > len(longest):
            longest = line
    return f'Longest list:  {longest} ->> [{longest[0]} , {longest[-1]}]'


# ls = []
# ls = [1, 5, 8, 2, 3, 4, 6, 1, 7]
# ls = [8, 2, 1, 12, 13, 9, 10, 11, 3, 4,  1, 7]
ls = [1, 5, 2, 3, 4,  1, 7, 8, 15, 1]

if not ls:
    print('List is empty')
    exit()
result_lst = []
for i in ls:
    result_lst.append(find_list(i, ls))
print(get_longest(result_lst))
