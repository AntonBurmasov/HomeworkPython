# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)




with open('polynom.txt', 'r') as data:
    record1 = data.read()

with open('polynom2.txt', 'r') as data:
    record2 = data.read()



print(record1)
print(record2)

lst1 = record1.split('+')
lst2 = record2.split('+')

lst1[-1] = lst1[-1].split('=', 1)[0]
lst2[-1] = lst2[-1].split('=', 1)[0]



new_polynom = ''

x1 = 0
y1 = 0
f1 = 0

i = 0
while i <= len(lst1)-1 :
    if i < len(lst1)-2:
        x1 = int(lst1[i].split('* x^', 1)[0])
        y1 = int(lst2[i].split('* x^', 1)[0])
        f1 = int(lst1[i].split('* x^', 2)[1])
        new_polynom += f'{x1 + y1} * x^{f1} + '
    elif i == len(lst1)-2:
        x1 = int(lst1[i].split('* x', 1)[0])
        y1 = int(lst2[i].split('* x', 1)[0])
        new_polynom += f'{x1 + y1} * x + '
    elif i == len(lst1) - 1:
        x1 = int(lst1[i])
        y1 = int(lst2[i])
        new_polynom += f'{x1 + y1} = 0'

    i += 1



print(new_polynom)

with open('new_polynom.txt', 'w') as data:
    data.write(new_polynom)
