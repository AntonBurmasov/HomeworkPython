# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#
#     *Пример:*
#
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

print("Введите  число.")
n = int(input())

dictionary = {}

x = 1
sum = 0

while x <= n:
    dictionary[x] = (1 + (1/x)) ** x
    sum = sum + dictionary[x]
    x += 1

print(dictionary)

print ("Сумма всех значений словаря равна "  "%.4f" % sum)

