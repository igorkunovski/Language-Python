# задача 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
# все конфеты у своего конкурента?
# Делаем игру против бота
#
# а) Подумайте как наделить бота ""интеллектом""

import random


def draw():
    # True - Human, False - computer
    return random.choice([True, False])


def insert_num():
    try:
        insert = int(input('Insert int number from 1 to 28 to take: '))
        if 1 > insert or insert > 28:
            print('Incorrect number. Must be within 1-28.')
            return insert_num()
        else:
            return insert
    except ValueError:
        print('Not a number or entered incorrectly.')
        exit()


# # DUMP computer method
# def comp_play(total: int):
#     comp_num = random.randint(1, 28)
#     print(f'-->Computer number is:  {comp_num}')
#     return comp_num


# SMART Computer method - if starts, always wins
def comp_play(total: int):
    check_win = total - (total // 28 * 28) - 1
    if check_win >= 0:
        comp_num = check_win
    else:
        comp_num = random.randint(1, 28)
    print(f'-->Computer number is:  {comp_num}')
    return comp_num


def game_round(player: bool, total: int):
    temp_total = insert_num() if player else comp_play(total)
    return temp_total


def game(total: int):
    input('press Enter to start the game: ')
    print('*** GAME START. Playing with numbers 1 - 28 ***')
    starter = draw()
    player = starter

    while total > 0:
        if total < 29:
            if player:
                return print(f'The HUMAN is winner!')
            else:
                return print(f'The COMPUTER is winner!')
        else:
            total -= game_round(player, total)
            print(f'***Total left {total}')
            player = not player
    return


if __name__ == '__main__':

    try:
        game(int(input('Please enter Total number to play: ')))
    except ValueError:
        print('Incorrect number, please check and start again.')
        exit()
