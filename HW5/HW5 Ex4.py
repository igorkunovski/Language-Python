# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2 -6*x-3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

def rem_whitespaces(line: str):
    return line.replace(' ', '')


def swap_minus(line: str):
    return line.replace('-', '+ -')


# добавление 1 перед *x если нет числа (x = 1*x)
def add_1(line: str):
    if line[0] == "x":
        line = "1*" + line
    for i in range(1, len(line)):
        if line[i] == "x" and (line[i - 1] == "+" or line[i - 1] == "-"):
            line = line[0:i] + "1*" + line[i:]
        elif line[i] == "x" and not line[i - 2].isdigit() and (line[i - 1] == "+" or line[i - 1] == "-"):
            line = line[0:i] + "1*" + line[i:]
    return line


# объединение строк в список
def inputs_to_list(line1: str, line2: str):
    line1 = line1.split("+")
    line2 = line2.split("+")
    return line1 + line2


# вычисление списка с числами без х
def calc_number(nums: list):
    number = 0
    for num in nums:
        number += int(num)
    if number > 0:
        return str(f' + {number}')
    return str(f' {number}')


# вычесление списка выражений, содержащих х в первой степени
def calc_part_x(with_x: list):
    number_x = 0
    for num in with_x:
        number_x += int(num.split("*x")[0])
    if number_x > 0:
        return str(f' + {number_x}x')
    return str(f' {number_x}x')


# вычисление списка с x со степенями >1
def calc_ratio_part(with_ratio: list):
    with_ratio = sorted(with_ratio, key=lambda x: x[-1], reverse=True)
    final = ''
    temp_num = 0
    for j in range(len(with_ratio) - 1):

        if with_ratio[j][-1] != with_ratio[j + 1][-1]:
            temp_num += int(with_ratio[j].split('*')[0])
            final += str(temp_num) + '*x^' + with_ratio[j][-1] + ' + '
            temp_num = 0
        else:
            temp_num += int(with_ratio[j].split('*')[0])

    temp_num += int(with_ratio[-1][0])
    final += str(temp_num) + '*x^' + with_ratio[-1][-1]
    return f'{final}'


# разделения общего списка на 3 списка для обработки, вычисление и формирование результата
def construct_result(total_input: list):
    part_num = []
    part_with_x = []
    part_ratio = []

    for i in total_input:
        if '^' in i:
            part_ratio.append(i)
        elif '^' not in i and 'x' in i:
            part_with_x.append(i)
        else:
            part_num.append(i)
    return f'{calc_ratio_part(part_ratio)}{calc_part_x(part_with_x)}{calc_number(part_num)} = 0'


if __name__ == '__main__':
    inp1 = input('Введите первое уравнение в формате Ax^n + Bx + C:  ')
    inp2 = input('Введите второе уравнение в формате Ax^n + Bx + C:  ')

    inp_list = [inp1, inp2]
    inp_list = list(map(lambda x: rem_whitespaces(x), inp_list))
    inp_list = list(map(lambda x: add_1(x), inp_list))
    inp_list = list(map(lambda x: swap_minus(x), inp_list))
    inp_list = inputs_to_list(inp_list[0], inp_list[1])
    inp_list = list(map(lambda x: rem_whitespaces(x), inp_list))

    print(f'RESULT: {construct_result(inp_list)}')
