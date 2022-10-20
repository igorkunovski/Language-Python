# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# a[k] * x ** k + ... ...+ a[2] * x ** 2 + a[1] * x ** 1 + a[0] * x ** 0 = 0

import random


def rand_rate():
    return random.randint(0, 101)


def factor_list(fact: int):
    lst = []
    for i in range(fact+1):
        lst.append(rand_rate())
    return lst


def create_data(fact_list: list):
    data = ''
    size = len(fact_list)

    if len(fact_list) > 1:
        for i in range(size):
            if i != size - 1 and i != size - 2 and fact_list[i] != 0:
                data += f'{fact_list[i]}x^{size - i - 1}'
                if fact_list[i + 1] != 0:
                    data += ' + '
            elif i == size - 2 and fact_list[i] != 0:
                data += f'{fact_list[i]}x'
                if fact_list[i + 1] != 0:
                    data += ' + '
            elif i == size - 1 and fact_list[i] != 0:
                data += f'{fact_list[i]} = 0'
            elif i == size - 1 and fact_list[i] == 0:
                data += ' = 0'
    else:
        data = 'x = 0'
    print(data)
    return data


def write_file(text: str):
    with open('ex3_file.txt', 'w') as data:
        data.write(text)


try:
    factor = int(input('Input factor: '))
except ValueError:
    print('Incorrect input!')
    exit()

ratio_list = factor_list(factor)
print(f'Ratio list : {ratio_list}')
write_file(create_data(ratio_list))

