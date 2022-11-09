# Задача 1. Создайте программу для игры в "Крестики-нолики".

import random


# создание поля игры - 2-х мерного массива
def generate_multi_list(rows: int, cols: int):
    multi_list = [['-' for col in range(0, cols)] for row in range(0, rows)]
    return multi_list


def print_multi_list(multi_dim_list: list):
    for line in multi_dim_list:
        print(str(line).replace(",", " ").replace("'", "").replace("[", "").replace("]", ""))
        # print(line)


# для удобства выбора человек вводит на поле в пределах от 1 до 3.
# Массив же меняется 0-2 (ячейка 3,3 ввода = 2,2 в массиве)
def human_move():
    row = int(input('Введите ряд: '))
    col = int(input('Введите колонку: '))
    if (0 < row < 4) and (0 < col < 4) and (field[row - 1][col - 1] == '-'):
        field[row - 1][col - 1] = 'X'
    else:
        print('занято или за пределами поля')
        print()
        human_move()


def comp_move():
    print('ход компьютера')
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col] == "-":
            field[row][col] = "0"
            break
        else:
            continue
    print_multi_list(field)


def check_win(lst: list, mark: str):
    if (
            (lst[0][0] == mark and lst[0][1] == mark and lst[0][2] == mark)
            or (lst[1][0] == mark and lst[1][1] == mark and lst[1][2] == mark)
            or (lst[2][0] == mark and lst[2][1] == mark and lst[2][2] == mark)
            or (lst[0][0] == mark and lst[1][0] == mark and lst[2][0] == mark)
            or (lst[0][1] == mark and lst[1][1] == mark and lst[2][1] == mark)
            or (lst[0][2] == mark and lst[1][2] == mark and lst[2][2] == mark)
            or (lst[0][0] == mark and lst[1][1] == mark and lst[2][2] == mark)
            or (lst[0][2] == mark and lst[1][1] == mark and lst[2][0] == mark)
    ):
        return True
    return False


def game(fld: list):
    counter = 0
    while counter < 9:
        human_move()
        if not check_win(fld, "X"):
            counter += 1
        else:
            print()
            print("**Победа человека**")
            print_multi_list(field)
            return

        # ход компьютера
        if counter < 9:
            comp_move()
            if not check_win(fld, "0"):
                counter += 1
            else:
                print()
                print("**Победа компьютера**")
                print_multi_list(field)
                return
    print_multi_list(field)
    print('Ничья')


field = generate_multi_list(3, 3)
print_multi_list(field)
game(field)
