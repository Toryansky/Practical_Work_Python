# Задача 2.Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input("Введите натуральное число: "))
saved_number = number
sp = []
divisor = 2
while divisor <= number:
    if (number % divisor) == 0:
        sp.append(divisor)
        number = number/divisor
    else:
        divisor += 1
print(f"Список простых множителей для числа {saved_number}: \n{sp}")
