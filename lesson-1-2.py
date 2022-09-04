# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def program(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (program(0, 0, 0) and program(0, 0, 1) and program(0, 1, 0) and program(0, 1, 1) and 
program(1, 0, 0) and program(1, 0, 1) and program(1, 1, 0) and program(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")