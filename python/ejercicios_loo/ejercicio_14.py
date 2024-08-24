""" Desarrollar un algoritmo que muestre los primeros n 
números primos siendo n un valor que debe ingresar el usuario.
"""


def es_primo(a):
    """devuelve true o false si a en primo o no"""
    i = 2
    while (a > i and i <= a and a % i != 0):
        i += 1
    return a == i


n = int(input("Ingrese la cantidad de primos: \n"))
contador_de_primos = 0

i = 2
while contador_de_primos < n:
    if es_primo(i):
        contador_de_primos += 1
        print(i)
    i += 1
