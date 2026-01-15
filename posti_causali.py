import random

coordinate = [
    "SxA", "SxB", "SyA", "SyB", "SzA", "SzB",
    "CxC", "CxD", "CyC", "CyD", "CzC", "CzD",
    "DxE", "DxF", "DxG", "DyE", "DyF", "DyG",
    "DzF", "DzG", "DaF", "DaG"
]

# Genera numeri unici da 1 a 22
numeri = list(range(1, 23))
random.shuffle(numeri)

for i, coord in enumerate(coordinate):
    print(f"{numeri[i]}.{coord}")
