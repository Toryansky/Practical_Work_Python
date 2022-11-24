# Задача 2.Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Проверка истинности утверждения" "\n¬(X⋁Y⋁Z) = ¬X⋀¬Y⋀¬Z" "\nдля всех предикатов: ")

for x in range(2):
    for y in range(2):
        for z in range(2):
            print([x, y, z], "\t", end="")

            if not (x or y or z) == (not x and not y and not z):
                print(True)
            else:
                print(False)
