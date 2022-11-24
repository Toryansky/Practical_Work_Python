# Задача 4.Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_quarter = int(input("Введите номер четверти: "))

if coordinate_quarter == 1:
    print("В этой четверти x > 0 и y > 0")
elif coordinate_quarter == 2:
    print("В этой четверти x < 0 и y > 0")
elif coordinate_quarter == 3:
    print("В этой четверти x < 0 и y < 0")
elif coordinate_quarter == 4:
    print("В этой четверти x > 0 и y < 0")
else:
    print("Координатной четверти с таким номером не существует")
