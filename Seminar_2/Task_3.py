# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведите на экран их сумму.

number = int(input("Введите число: "))

print(f"Ваша последовательность для числа {number}: ")

for i in range(1, number + 1, 1):
    print(round((1 + 1/i)**i, 4), end=" | ")

summa = 0
for i in range(1, number + 1):
    summa += (1 + 1/i)**i
print(f"\nСумма последовательности равна: {summa:.4f}")
