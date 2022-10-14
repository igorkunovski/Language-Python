# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def count_str_entry():

    str1 = input('Insert string 1: ')
    str2 = input('Insert string 2: ')
    counter = 0

    if len(str2) > len(str1):
        str1, str2 = str2, str1

    for num in range(len(str1)):
        if str2[0] == str1[num]:
            if str1[num:len(str2) + num:] == str2:
                counter += 1
    return counter


print(count_str_entry())
