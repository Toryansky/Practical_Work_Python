# Задача 5.Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

import math

coordinate_x_A = int(input("Введите координату X точки A: "))
coordinate_y_A = int(input("Введите координату Y точки A: "))
coordinate_x_B = int(input("Введите координату X точки B: "))
coordinate_y_B = int(input("Введите координату Y точки B: "))

distance_AB = math.sqrt((coordinate_x_A - coordinate_x_B) ** 2 + (coordinate_y_A - coordinate_y_B) ** 2)

print(f"Расстояние между точками A и B: {distance_AB:.2f}")
