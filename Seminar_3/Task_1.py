# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

n = int(input("Введите количество элементов списка N: "))

sp = []
for i in range(n):
    element = (randint(-10, 10))
    sp.append(element)
print(f"Ваш список: {sp}")

summa = 0
for j in range(1, n, 2):
    summa = summa + sp[j]

print(f"Сумма элементов, стоящих на нечётной позиции: {summa}")
