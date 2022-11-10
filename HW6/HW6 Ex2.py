# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

def whitespaces_remove(line: str):
    return line.replace(' ', '')


def replace_minus(line: str):
    return line.replace('-', '+ -')


def split_by_plus(line: str):
    lst = line.split("+")
    return lst


def calculation(st_lst: list):
    result = 0
    for exp in st_lst:

        if "*" not in exp and "/" not in exp:
            result += int(exp)

        elif "*" in exp and "/" not in exp:
            temp_lst = exp.split("*")
            temp = 1
            for j in temp_lst:
                temp *= int(j)
            result += temp

        elif "*" not in exp and "/" in exp:
            temp_lst = exp.split("/")
            temp = int(temp_lst[0])
            for j in range(1, len(temp_lst)):
                temp /= int(temp_lst[j])
            result += temp

        elif "*" in exp and "/" in exp:
            mult_lst = exp.split("*")

            dev_lst = []

            for i in mult_lst:
                temp_lst = i.split("/")
                temp = int(temp_lst[0])
                for j in range(1, len(temp_lst)):
                    if int(temp_lst[j]) != 0:
                        temp /= int(temp_lst[j])
                    else:
                        return ArithmeticError("Arithmetic Error - division by 0.")
                dev_lst.append(str(temp))

            tmp_res = 1
            for k in dev_lst:
                tmp_res *= float(str(k))
            result += tmp_res
    return result


def brackets_remove(st: str):

    while "(" in st or ")" in st:
        substrings = ""
        left = st.index("(")
        right = st.index(")")
        substrings += st[0:left]
        substrings += str(calculation(split_by_plus(st[left + 1:right])))
        substrings += st[right + 1:]
        st = substrings
        # print(st)
    return st


def if_brackets(st: str):
    if "(" in st or ")" in st:
        return True
    return False


# input_string = "16/4*2/2*3"    # => 12
input_string = "1 + (1 + 2) * 6 / (3 - 3)"  # => Result =  Arithmetic Error - division by 0.
# input_string = "1 - 2*3 - 8/2 + 2"  # => -7
# input_string = "(1+2)*3"  # => 9

print(input_string)
input_string = whitespaces_remove(input_string)
input_string = replace_minus(input_string)

if if_brackets(input_string):
    input_string = brackets_remove(input_string)

list_to_calculate = split_by_plus(input_string)
print(f'Result =  {calculation(list_to_calculate)}')
