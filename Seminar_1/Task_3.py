# Задача 3.Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

parameter_x = int(input("Введите значение X: "))
parameter_y = int(input("Введите значение Y: "))

if parameter_y > 0:
    if parameter_x > 0:
        print("Точка находится в 1 четверти")
    if parameter_x < 0:
        print("Точка находится во 2 четверти")

if parameter_y < 0:
    if parameter_x < 0:
        print("Точка находится в 3 четверти")
    if parameter_x > 0:
        print("Точка находится в 4 четверти")

if parameter_y == 0:
    if parameter_x != 0:
        print("Точка находится на оси OX")

if parameter_x == 0:
    if parameter_y != 0:
        print("Точка находится на оси OY")

if parameter_x == 0:
    if parameter_y == 0:
        print("Это начало координат")
