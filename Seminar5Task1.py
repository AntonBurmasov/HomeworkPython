# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random

type_of_game = int(input("Выберите режим игры, введите 1 для одиночной игры против компьютер, 2 - для игры против другого игрока."))
order = random.randint(0, 1)
if type_of_game == 1:
    print("Дано 200 конфет,  игрок и компьютер могут брать не больше 28 конфет, кто заберет последние- выигрывает.")
    candys = 200


    if order == 0:
        print("Первым ходит игрок.")
        while candys > 0:
            minus = int(input("Введите, сколько конфет вычесть из общей суммы"))
            if minus < 29 and minus > 0:

                candys = candys - minus
                print(f"Игрок забрал {minus} конфет.Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus = int(input("Введите, сколько конфет вычесть из общей суммы: "))
                if minus < 29 and minus > 0:
                    candys = candys - minus
                    print(f"Игрок забрал {minus} конфет.Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок")
                exit()
            PC_candys = candys % 29
            candys = candys - PC_candys
            print(f"Пк забрал {PC_candys} конфет. Осталось конфет {candys}")

            if candys == 0 or candys < 0:
                print("Победил компьютер")
                exit()

    else:
        print("Первым ходит компьютер")
        while candys > 0:
            PC_candys = candys % 29
            candys = candys - PC_candys
            print(f"Пк забрал {PC_candys} конфет.Осталось конфет {candys}")
            if candys == 0 or candys < 0:
                print("Победил компьютер")
                exit()

            minus_candys = int(input("Введите, сколько конфет вычесть из общей суммы"))
            if minus_candys < 29 and minus_candys > 0:
                candys = candys - minus_candys
                print(f"Игрок забрал {minus_candys} конфет.Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus_candys = int(input("Введите, сколько конфет вычесть из общей суммы: "))
                if minus_candys < 29 and minus_candys > 0:
                    candys = candys - minus_candys
                    print(f"Игрок забрал {minus_candys} конфет.Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок")
                exit()

elif type_of_game == 2:
    print("Дано 200 конфет,  игроки могут брать не больше 28 конфет, кто заберет последние- выигрывает.")
    candys = 200

    if order == 0:
        print("Первым ходит игрок 1.")
        while candys > 0:
            minus_candys = int(input("Первый игрок, введите, сколько конфет вычесть из общей суммы: "))
            if minus_candys < 29 and minus_candys > 0:
                candys = candys - minus_candys
                print(f"Игрок 1 забрал {minus_candys} конфет. Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus_candys = int(input("Первыйц игрок, введите, сколько конфет вычесть из общей суммы: "))
                if minus_candys < 29 and minus_candys > 0:
                    candys = candys - minus_candys
                    print(f"Игрок забрал {minus_candys} конфет.Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок 1")
                exit()
            minus_second = int(input("Второй игрок, введите, сколько конфет вычесть из общей суммы: "))
            if minus_second < 29 and minus_second > 0:
                candys = candys - minus_second
                print(f"Игрок 2 забрал {minus_second} конфет. Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus_second = int(input("Второй игрок, введите, сколько конфет вычесть из общей суммы: "))
                if minus_second < 29 and minus_second > 0:
                    candys = candys - minus_second
                    print(f"Игрок 2 забрал {minus_second} конфет. Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок 2")
                exit()
    else:
        print("Первым ходит игрок 2.")
        while candys > 0:
            minus_candys = int(input("Второй игрок, введите, сколько конфет вычесть из общей суммы: "))
            if minus_candys < 29 and minus_candys > 0:
                candys = candys - minus_candys
                print(f"Игрок 2 забрал {minus_candys} конфет. Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus_candys = int(input("Второй игрок, введите, сколько конфет вычесть из общей суммы: "))
                if minus_candys < 29 and minus_candys > 0:
                    candys = candys - minus_candys
                    print(f"Игрок 2 забрал {minus_candys} конфет. Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок 2")
                exit()
            minus_second = int(input("Первый игрок, введите, сколько конфет вычесть из общей суммы: "))
            if minus_second < 29 and minus_second > 0:
                candys = candys - minus_second
                print(f"Игрок 1 забрал {minus_second} конфет. Осталось конфет {candys}")
            else:
                print("Число вычитаемых конфет должно быть от 1 до 28")
                minus_second = int(input("Первый игрок, введите, сколько конфет вычесть из общей суммы: "))
                if minus_second < 29 and minus_second > 0:
                    candys = candys - minus_second
                    print(f"Игрок 1 забрал {minus_second} конфет. Осталось конфет {candys}")
                else:
                    print("Вы нарушаете правила игры, игра окончена.")
                    exit()

            if candys == 0 or candys < 0:
                print("Победил игрок 1")
                exit()

else:
    print("Режим игры может быть только 1 или 2.")
    exit()




