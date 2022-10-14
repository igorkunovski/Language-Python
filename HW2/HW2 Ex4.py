# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на
# вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

import math


def find_distance():
    dimension = int(input('Please insert dimensions int number N = '))
    coordinate_a = []
    distance = 0
    for i in range(dimension):
        coordinate_a.append(int(input('Insert coordinates of point A for the dimension (' + str(dimension) + ') : ')))

    coordinate_b = []
    for i in range(dimension):
        coordinate_b.append(int(input('Insert coordinates of point B: ')))

    print('Point coordinate is: ' + str(coordinate_a), coordinate_b)

    for i in range(dimension):
        distance += math.sqrt((coordinate_b[i] - coordinate_a[i]) ** 2)

    return round(distance, 3)


try:
    print('Distance is: ' + str(find_distance()))
except:
    print('Введите числа')
