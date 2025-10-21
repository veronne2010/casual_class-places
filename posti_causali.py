import random

coordinate = [
    "SxA", "SxB", "SyA", "SyB", "SzA", "SzB",
    "CxC", "CxD", "CyC", "CyD", "CzC", "CzD",
    "DxE", "DxF", "DxG", "DyE", "DyF", "DyG",
    "DzE", "DzF", "DzG", "DaF", "DaG"
]

# Genera un numero casuale da 1 a 23 per ogni coordinata
for coord in coordinate:
    numero = random.randint(1, 23)
    print(f"{numero}.{coord}")
