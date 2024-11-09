"""Leer enteros y hacer una sumatoria"""

with open("enteros.in", "r", encoding="utf-8") as file:
    suma = 0
    for numero in file:
        suma += int(numero)
        print("suma parcial: ", suma)

print("\nSuma total: ", suma)
