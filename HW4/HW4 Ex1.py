# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factors():
    result = []
    for i in range(1, abs(num) + 1):
        if abs(num) % i == 0:
            result.append(i)
    return result


try:
    num = int(input('Insert int number to find factors: '))
except ValueError:
    print('Incorrect number!')
    exit()
print('Factors are : ' + str(factors()))







