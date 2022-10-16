# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# - 66 -> 1000010
# - -66 -> -1000010

def dec_to_bin_converter():
    try:
        num_dec = int(input('Insert int number: '))
    except ValueError:
        print('Not an int number! ')
        exit()

    result_str = ''
    result_start = ''

    if num_dec < 0:
        result_start = '-'
        num_dec = abs(num_dec)

    while num_dec != 0:
        result_str += str((num_dec % 2))
        num_dec = num_dec // 2
    return result_start + result_str[::-1]


print(dec_to_bin_converter())

