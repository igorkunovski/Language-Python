# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
#
# *Пример:*
#
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
# x=-4; y=3 -> 2

def find_quarter(x: int, y: int):
    if x == 0 and y == 0:
        return 'center!'
    elif x >= 0 <= y:
        return 1
    elif x >= 0 >= y:
        return 4
    elif x <= 0 >= y:
        return 3
    elif x <= 0 <= y:
        return 2

try:
    x = int(input('Please insert x: '))
    y = int(input('Please insert y: '))
    print(find_quarter(x, y))
except:
    print('Not a number!')
