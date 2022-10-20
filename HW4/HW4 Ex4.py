# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений.
# 0*x^2+5*x+6=0
# 60*x^2-50*x+6=0

# Ax² + Bx + C = 0

def input_read():
    user_input = input('Введите уравнение Ax² + Bx + C = 0 в формате Ax^2 + Bx + C = 0:  ')
    # удаляем возможные пробелы ввода
    user_input = user_input.replace(' ', '')
    # меняю возможные минусы уравнения на + (-число)
    user_input = user_input.replace('-', '+ -')
    # делим уравнение по (=) и потом левую часть от (=) по (+)
    lst_eq = user_input.split('=')[0].split('+')
    # получаем список коэффицентов, убирая (х) и правую часть от (х - степени^ )
    num_list = []
    for elem in lst_eq:
        num_list.append(elem.split('*x')[0])
    print(f'коэффиценты уравнения : {num_list}')
    return num_list


def calculation(input_list: list):
    if len(input_list) == 3:
        try:
            a = int((input_list[0]))
            b = int((input_list[1]))
            c = int((input_list[2]))
        except ValueError:
            # если split не помогли избавиться от лишнего
            print('Ошибки при вводе уравнения')
            exit()

        if a != 0:
            # дискриминант d
            d = b**2 - 4*a*c
            if d > 0:
                print(f' D = {d}')
                print(f'Имеет два решения {round((-b + d**0.5) / 2*a, 3)} и {round((-b - d**0.5) / 2*a, 3)}')
            elif d < 0:
                print(f' D = {d}')
                print('Нет решений')
            else:
                print(f' D = {d}')
                print(f'есть одно решение  {round(-b / 2 * a, 3)}')
        else:
            print('A = 0')
            print(f'Линейное уравнение: x = -B - C =  {-b -c}')
    else:
        print('Ошибка при вводе уравнения')


calculation(input_read())
