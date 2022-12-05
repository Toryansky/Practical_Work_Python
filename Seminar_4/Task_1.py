# Задача 1.Вычислить число c заданной точностью d

from math import pi

accuracy = int(input("Введите желаемую точность числа Пи: "))
print(f"Число Пи с заданной точностью равно: {round(pi, accuracy)}")
