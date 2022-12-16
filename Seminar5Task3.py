# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(s):
    encoding = ""  # сохраняет выходную строку

    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1

    return encoding


def decode(s):
    decoding = ""
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''

    return decoding


string = 'AAAARRRRRRRFFFFFFFFFFFFFCDDDDDDDDDDDDD'
print(string)
coded_string = (encode(string))
print(coded_string)
print(decode(coded_string))
