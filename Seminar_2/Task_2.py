# Задача 2.Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

import math

number = int(input("Введите число: "))
if number >= 1:
    print(f"Ваш набор произведений для числа {number}: ")
else:
    print("Введенное число вне диапазона.")
for i in range(1, number + 1, 1):
    print(math.factorial(i), end="\t")
