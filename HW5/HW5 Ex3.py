# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

text = "Играют два игроабвка делая абв ход друг после друга. Первый ход абвопределяется жереаббьвёвкой. " \
       "За один ход моабжвно забратьабв не более чем абв28 конфет."


def remove_searched(search: str, txt: str):
    text_result = []
    text_lst = txt.split()
    for i in text_lst:
        if search not in i:
            text_result.append(i)
    return str(''.join(str(text_result))).replace(',', '').replace("'", '')[1:-1]


if __name__ == '__main__':
    print(remove_searched('абв', text))
