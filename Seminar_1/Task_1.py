# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

keep_checking = "д"

while keep_checking == "д":

    weekday = int(input("Введите цифру, соответствующую дню недели: "))

    if 1 <= weekday <= 5:
        print("Этот день не выходной")
    elif weekday == 6 or weekday == 7:
        print("Этот день выходной")
    else:
        print("Введённое число вне диапазона")
    keep_checking = input("Нажмите д, если хотите продолжать проверку: ")
