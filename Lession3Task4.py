# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

print("Введите десятичное число.")

number = int(input())

binary_number = ""
if number == 0:
    print(number)


while number > 0:
    variable = str(number % 2)
    binary_number = variable + binary_number
    number = int(number / 2)

print(binary_number)