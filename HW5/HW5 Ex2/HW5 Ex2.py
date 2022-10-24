# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Кодирование длин серий (RLE) в Python – это форма сжатия данных, в которой поток данных
# предоставляется в качестве входных данных (например, «AAABBCCCC»), а выходными данными является последовательность
# отсчетов последовательных значений данных в строке (3A2B4C)


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        # If the prev and current characters don't match...
        if char != prev_char:
            # ...then add the count and character to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            # count clear to 1 to start seria from the beginning
            count = 1
            prev_char = char
        else:
        # Or increment our counter if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical character and need to expand it for the decoding
            decode += char * int(count)
            count = ''
    return decode


f = open("encoded.txt", "r", encoding="utf8")
print('--DECODING--')
for line in f:
    print(rle_decode(line[0:-1]))
f.close()

f = open("decoded.txt", "r", encoding="utf8")
print('--ENCODING--')
for line in f:
    print(rle_encode(line[0:-1]))
f.close()

# # encoded_val = rle_encode('AAAAAFDDCCCCCCCAEEE')
# # print(encoded_val)
# #
# # decoded_val = rle_decode('6A1F2D7C1A3E')
# # print(decoded_val)
