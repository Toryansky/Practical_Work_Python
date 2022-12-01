# Задача 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

n = int(input("Введите количество чисел последовательности: "))

sp_positive = [1, 1]
for i in range(2, n):
    element_pos = sp_positive[i-2] + sp_positive[i-1]
    sp_positive.append(element_pos)

sp_negative = []
for j in range(len(sp_positive)):
    element_neg = (-1) ** j * sp_positive[j]
    sp_negative.append(element_neg)

sp_merged = sp_negative[::-1] + [0] + sp_positive

print(f"Ваш список чисел Фибоначчи: {sp_merged}")
