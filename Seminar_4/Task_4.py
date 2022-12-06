# Задача 4.Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

exponent = int(input("Введите степень многочлена: "))
sp_coeff = []
for i in range(0, exponent+1):
    sp_coeff.append(random.randint(0, 100))

print(f"Список коэффициентов: {sp_coeff}")

sp_components = []

for i in range(len(sp_coeff)):
    if sp_coeff[i] > 1:
        if (len(sp_coeff) - i - 1) > 1:
            sp_components.append(f"{sp_coeff[i]}x^{(len(sp_coeff) - i - 1)}")
        if (len(sp_coeff) - i - 1) == 1:
            sp_components.append(f"{sp_coeff[i]}x")
        if (len(sp_coeff) - i - 1) == 0:
            sp_components.append(f"{sp_coeff[i]}")
    elif sp_coeff[i] == 1:
        if (len(sp_coeff) - i - 1) > 1:
            sp_components.append(f"x^{len(sp_coeff) - i - 1}")
        if (len(sp_coeff) - i - 1) == 1:
            sp_components.append(f"x")
        if (len(sp_coeff) - i - 1) == 0:
            sp_components.append(f"{sp_coeff[i]}")

if len(sp_components) == 0:
    sp_components.append("0")

polinomial = " + ".join(sp_components)
print(f"Многочлен {exponent}-й степени: {polinomial}. Записан в файл: polinom.txt")

with open("polinom.txt", "w") as data:
    data.write(str(polinomial))
