# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.(Сделать для строки)
#
#     *Пример:*
#
#     - 6782 -> 23
#     - 0,56 -> 11



print("Введите вещественное число.")
n = str(input())

if "." not in n:
    print("Вы ввели невещественное число.")
    exit()


num = str(n).split('.')

whole = int(num[0])

if whole < 0:
    whole = abs(whole)


remainder = int(num[-1])



sum1 = 0

while whole >= 100:
    sum1 = sum1 + (whole % 10)
    whole = whole // 10


if whole < 100:
    sum1 = sum1 + (whole % 10)
    whole = whole // 10
    sum1 = sum1 + whole


sum2 = 0

while remainder >= 100:
    sum2 = sum2 + (remainder % 10)
    remainder = remainder // 10


if remainder < 100:
    sum2 = sum2 + (remainder % 10)
    remainder = remainder // 10
    sum2 = sum2 + remainder

sum = str(sum1 + sum2)

print(sum)

