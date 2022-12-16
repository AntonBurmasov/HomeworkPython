# Создайте программу для игры в ""Крестики-нолики"".

import random

field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

print(
    "Первый игрок ставит кресты(x), второй игрок- нули (0), победит тот игрок, котогрый первый составит ряд из своих фигур.")

order = random.randint(0, 1)

print("Первым ходит игрок 1.")
print(*field, sep="\n")
variable = 0
while variable < 9:
    print("Игрок 1, введите координату, на которую вы хотите поставить фигуру, значения от 0 до 2.")
    x = int(input("Введите расположение по вертикали: "))
    y = int(input("Введите расположение по горизонтали: "))
    if x > -1 and x < 3 and y > -1 and y < 3:
        if field[x][y] != 'x' and field[x][y] != '0':
            field[x][y] = 'x'
    else:
        print("Вы ввели координату, выходящую за диапазон игрового поля")
        print("Игрок 1, введите координату, на которую вы хотите поставить фигуру, значения от 0 до 2.")
        x = int(input("Введите расположение по вертикали: "))
        y = int(input("Введите расположение по горизонтали: "))
        if x > -1 and x < 3 and y > -1 and y < 3:
            if field[x][y] != 'x' and field[x][y] != '0':
                field[x][y] = 'x'
        else:
            print("Вы вводите координаты неверно, игра закончена.")
            exit()
    if (field[0][0] == 'x' and field[0][1] == 'x' and field[0][2] == 'x' or
            field[1][0] == 'x' and field[1][1] == 'x' and field[1][2] == 'x' or
            field[2][0] == 'x' and field[2][1] == 'x' and field[2][2] == 'x' or
            field[0][0] == 'x' and field[1][0] == 'x' and field[2][0] == 'x' or
            field[0][1] == 'x' and field[1][1] == 'x' and field[2][1] == 'x' or
            field[0][2] == 'x' and field[1][2] == 'x' and field[2][2] == 'x' or
            field[0][0] == 'x' and field[1][1] == 'x' and field[2][2] == 'x' or
            field[2][0] == 'x' and field[1][1] == 'x' and field[0][2] == 'x'):
        print("Победил игрок 1")
        print(*field, sep="\n")
        exit()
    print(*field, sep="\n")

    print("Игрок 2, введите координату, на которую вы хотите поставить фигуру")
    x = int(input("Введите расположение по вертикали: "))
    y = int(input("Введите расположение по горизонтали: "))
    if x > -1 and x < 3 and y > -1 and y < 3:
        if field[x][y] != 'x' and field[x][y] != '0':
            field[x][y] = '0'
    else:
        print("Вы ввели координату, выходящую за диапазон игрового поля")
        print("Игрок 2, введите координату, на которую вы хотите поставить фигуру, значения от 0 до 2.")
        x = int(input("Введите расположение по вертикали: "))
        y = int(input("Введите расположение по горизонтали: "))
        if x > -1 and x < 3 and y > -1 and y < 3:
            if field[x][y] != 'x' and field[x][y] != '0':
                field[x][y] = '0'
        else:
            print("Вы вводите координаты неверно, игра закончена.")
            exit()
    if (field[0][0] == '0' and field[0][1] == '0' and field[0][2] == '0' or
            field[1][0] == '0' and field[1][1] == '0' and field[1][2] == '0' or
            field[2][0] == '0' and field[2][1] == '0' and field[2][2] == '0' or
            field[0][0] == '0' and field[1][0] == '0' and field[2][0] == '0' or
            field[0][1] == '0' and field[1][1] == '0' and field[2][1] == '0' or
            field[0][2] == '0' and field[1][2] == '0' and field[2][2] == '0' or
            field[0][0] == '0' and field[1][1] == '0' and field[2][2] == '0' or
            field[2][0] == '0' and field[1][1] == '0' and field[0][2] == '0'):
        print("Победил игрок 2")
        print(*field, sep="\n")
        exit()
    print(*field, sep="\n")
    variable += 1




print("У игроков ничья.")
print(*field, sep="\n")
