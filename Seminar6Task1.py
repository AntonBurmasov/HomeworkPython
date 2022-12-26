# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка
# стоящих на нечётной позиции.
#
# Пример:
#
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


def f_rand(i):
    return random.randint(1, 101)


lst = [f_rand(i) for i in range(1, 11)]

print(lst)

sum_odd = 0
i = 1

while i < len(lst):
    sum_odd = sum_odd + lst[i]
    i += 2

print(sum_odd)
