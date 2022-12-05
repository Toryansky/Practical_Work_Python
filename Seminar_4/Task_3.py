# Задача 3.Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

number = int(input("Введите количество элементов списка N: "))

sp_original = []
for i in range(number):
    element = (randint(-10, 11))
    sp_original.append(element)
print(f"Исходная последовательность чисел: {sp_original}")

sp_final = []
for x in sp_original:
    if sp_original.count(x) == 1:
        sp_final.append(x)

print(f"Список неповторяющихся элементов: {sp_final}")
