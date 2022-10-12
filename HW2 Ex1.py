# Задача 1. Напишите программу, которая принимает на вход вещественное или
# целое число и показывает сумму его цифр. Через строку нельзя решать.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits():
    number_inserted = float(input("Введите число: "))

    number_int_part = int(number_inserted)
    number_float_part = number_inserted - number_int_part
    number_float_part = round(number_float_part, 3)
    sum1 = 0
    sum2 = 0

    while number_int_part > 0:
        sum1 += number_int_part % 10
        number_int_part //= 10

    if number_float_part > 0:
        while number_float_part != 0:
            sum2 = sum2 + int(number_float_part * 10)
            number_float_part = round((number_float_part * 10 - int(number_float_part * 10)), 3)
        return sum2 + sum1
    else:
        return sum1


print(sum_of_digits())
