# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]


lst = [4,7,6,-4,6,0,35,4,6,7,8]

print(lst)

new_lst = []

i = 0
while i < len(lst):
    if lst[i] not in new_lst:
        new_lst.append(lst[i])
        lst[i] = ""
    i += 1

j = 0
while j < len(new_lst):
    if new_lst[j] in lst:
        del new_lst[j]
        j -= 1

    j += 1


print(new_lst)






