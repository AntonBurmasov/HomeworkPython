# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.
#
#     *Пример:*
#
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print("Введите  число.")
n = int(input())

if n >= 1:
    sum = 1
    x = 2
    while x <= n:
        sum = sum * x
        x += 1
        print(sum, end=' ')


else:
   print("Число должно быть больше 1.")