# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication(number: int):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return number * multiplication(number - 1)


def list_of_multiplications():
    size = int(input('Please insert int number of list size: '))
    result_list = []
    for num in range(1, size + 1):
        result_list.append(multiplication(num))
    return result_list


try:
    print(list_of_multiplications())
except:
    print('Incorrect number! Please check')
