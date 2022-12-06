# Задача 1.Вычислить число c заданной точностью d

from math import pi

d = input("Введите желаемую точность числа Пи: ")
accuracy = d[::-1].find('.')
print(f"Число Пи с заданной точностью равно: {round(pi, accuracy)}")
