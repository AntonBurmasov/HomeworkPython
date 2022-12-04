# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19


import decimal
decimal.getcontext( ).prec = 2
list = [6.1, 4, 6.12, 5.6, 8, 4.01, 6.2]
variable = 0
min = decimal.Decimal(list[0]) % 1
max = decimal.Decimal(list[0]) % 1
print(min)
print(max)
for i in list:
    variable = decimal.Decimal(i) % 1
    if variable > max:
        max = variable
    if variable > 0:
        if variable < min:
            min = variable

print(max - min)
