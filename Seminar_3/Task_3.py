# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

import random

n = int(input("Введите количество элементов списка: "))
sp = []
for i in range(n):
    element = round((random.random() * 10), 2)
    sp.append(element)
print(f"Ваш список: {sp}")
fractional_sp = []
for j in range(len(sp)):
    if (sp[j] - int(sp[j])) > 0:
        fractional_sp.append((sp[j] - int(sp[j])))
diff = max(fractional_sp) - min(fractional_sp)
print(f"Разность между max и min значением дробной части элементов: {diff:.2f}")
