# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа

N = int(input("Введите число:"))

lst = []
d = 2
while d * d <= N:
    if N % d == 0:
        lst.append(d)
        N //= d
    else:
        d += 1

if N > 1:
    lst.append(N)


print(lst)