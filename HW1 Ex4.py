# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с
# пользовательского ввода три строки: первое число, второе число и операцию, после чего
# применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

import string


def calculate(number1: float, number2: float, action: string):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number == 0:
            return 'Division by 0!'
        else:
            return first_number / second_number
    elif operation == 'mod':
        if second_number == 0:
            return 'Division by 0!'
        else:
            return first_number % second_number
    elif operation == 'div':
        if second_number == 0:
            return 'Division by 0!'
        else:
            return int(first_number / second_number)
    elif operation == 'pow':
        return pow(first_number, second_number)
    else:
        return 'Incorrect action!'


try:
    first_number = float(input('Please insert first number: '))
    second_number = float(input('Please insert second number: '))
    operation = input('Please select operation +, -, /, *, mod, pow, div to be done: ')
    print(calculate(first_number, second_number, operation))
except:
    print('Not a number!')
