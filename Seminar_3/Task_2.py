# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

n = int(input("Введите количество элементов списка N: "))

sp = []
for i in range(n):
    element = (randint(-10, 10))
    sp.append(element)
print(f"Ваш список: {sp}")

sp2 = []
if n % 2 == 0:
    for j in range(n//2):
        x = sp[j] * sp[n-1-j]
        sp2.append(x)
    print(f"Произведение пар чисел списка: {sp2}")
else:
    for j in range(n//2+1):
        x = sp[j] * sp[n-1-j]
        sp2.append(x)
    print(f"Произведение пар чисел списка: {sp2}")
