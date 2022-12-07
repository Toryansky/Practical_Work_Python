# Задача 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open("file_1_for_task5.txt", "r") as data:
    polynomial_first = data.readline()

with open("file_2_for_task5.txt", "r") as data:
    polynomial_second = data.readline()

dict_first = {}
dict_second = {}
polynomial_first = polynomial_first.replace(" + ", " ").split()
polynomial_second = polynomial_second.replace(" + ", " ").split()

for i in range(len(polynomial_first)):
    polynomial_first[i] = polynomial_first[i].replace("+", "").split("x^")
    dict_first[int(polynomial_first[i][1])] = int(polynomial_first[i][0])
for i in range(len(polynomial_second)):
    polynomial_second[i] = polynomial_second[i].replace("+", "").split("x^")
    dict_second[int(polynomial_second[i][1])] = int(polynomial_second[i][0])

summary_dict = {}
max_key_value = (max(max(dict_first), max(dict_second)))
for i in range(max_key_value, 0, -1):
    summary_dict[i] = dict_first[i] + dict_second[i]

print(f"Степени и коэффициенты первого многочлена: {dict_first}")
print(f"Степени и коэффициенты второго многочлена: {dict_second}")
print(f"Степени и коэффициенты суммы многочленов: {summary_dict}")

polynomial_result = ""
for i in summary_dict.items():
    if polynomial_result == "":
        polynomial_result += str(abs(i[1])) + "x^" + str(abs(i[0]))
    else:
        polynomial_result += " + " + str(abs(i[1])) + "x^" + str(abs(i[0]))

print(f"Сумма многочленов: {polynomial_result}")

with open("polynomial_result.txt", "w") as data:
    data.write(polynomial_result)
