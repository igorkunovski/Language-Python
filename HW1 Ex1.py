# задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def if_weekend(day_number: int):
    if day == 6 or day == 7:
        return "да"
    elif day > 7 or day < 1:
        return 'Incorrect day of the week'
    else:
        return "нет"


try:
    day = int(input('Please insert day number: '))
    print(if_weekend(day))
except:
    print('Not a number!')
