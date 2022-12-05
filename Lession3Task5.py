# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

print("Введите число.")

n = int(input())

fibonacci = []

fibonacci.append(0)
fibonacci.append(1)
variable = 0

i = 2
while i <= n:
     variable = fibonacci[i - 1] + fibonacci[i - 2]
     fibonacci.append(variable)
     i = i + 1
     print(fibonacci)


fibonacci.insert(0, 1)

j = 3
while j <= n * 2:
     fibonacci.insert(0, fibonacci[j] * -1 )
     j = j + 2


print(fibonacci)