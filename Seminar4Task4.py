# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#
#     *Пример:*
#
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

import random

k = int(input("Задайте натуральную степень:"))


number = [random.randint(1, 100) for i in range(0, k + 1)]
print(number)

polynom = ''

for i in range(0, k + 1):
    if k - i > 1:
        polynom += f'{number[i]} * x^{k - i} + '
    elif k - i == 1:
        polynom += f'{number[i]} * x + '
    else:
        polynom += f'{number[i]} = 0'

print(polynom)

with open('polynom.txt', 'w') as data:
    data.write(polynom)







