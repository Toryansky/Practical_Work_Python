# Задача 4.Напишите программу, которая будет преобразовывать десятичное
# число в двоичное (встроенными методами пользоваться нельзя).

number = int(input("Введите десятичное число для преобразования: "))
sp = []
if number > 0:
    while number != 0:
        binary_digit_value = number % 2
        sp.append(str(binary_digit_value))
        number = number // 2
    print(f"Двоичная форма: " + "".join(sp[::-1]))
else:
    print(f"Двоичная форма: 0")
