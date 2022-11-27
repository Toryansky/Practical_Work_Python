# Задача 5.Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя,
# другие методы из библиотеки random - можно).

import random
from random import randint

elements_quantity = int(input("Введите количество элементов списка: "))
starting_sp = []
for i in range(elements_quantity):
    element = (randint(0, 10))
    starting_sp.append(element)
print(f"Исходный список: {starting_sp}")

mixed_sp = []
for j in range(len(starting_sp)):
    random_element = random.choice(starting_sp)
    mixed_sp.append(random_element)
    starting_sp.remove(random_element)

print(f"Перемешанный список: {mixed_sp}")
