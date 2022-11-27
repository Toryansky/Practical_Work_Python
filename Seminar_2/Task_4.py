# Задача 4.Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.

from random import randint

n = int(input("Введите количество элементов списка N: "))

# Запись в файл file.txt трех
# случайных индексов элементов
with open("file.txt", "w") as data:
    for index in (randint(0, n-1) for i in range(3)):
        data.write(str(index) + "\n")

print("Ваш список: ", end="")
sp = []
for j in range(n):
    element = (randint(-n, n))
    sp.append(element)
print(sp)

print("Позиции элементов: ", end="")

with open("file.txt", "r") as data:
    index_1 = int(data.readline())
    print(index_1, end=",")
    index_2 = int(data.readline())
    print(index_2, end=",")
    index_3 = int(data.readline())
    print(index_3)

print(f"Произведение элементов: {sp[index_1] * sp[index_2] * sp[index_3]}")
