""" Escribir una función que reciba dos arreglos a1 y a2, de enteros ordenados de menor a
    mayor e intercale los elementos de los arreglos que recibe en un nuevo arreglo, 
    tal que el arreglo resultante también esté ordenado. 
    Por ejemplo:
    a1 = [-5, 0, 0, 1, 5]
    a2 = [-10, 0, 7]
    resultado = [-10, -5, 0, 0, 0, 1, 5, 7]
"""


def mezcla(a, b) -> list:
    """funcion que mezcla los elementos de dos listas ordenadas,
    de manera tal que el resultado quede ordenado"""
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    if i == len(a):
        for v in range(j, len(b)):
            resultado.append(b[v])
    else:
        for v in range(i, len(a)):
            resultado.append(a[v])
    return resultado


# Main


a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]
# resultado = [-10, -5, 0, 0, 0, 1, 5, 7]
print(mezcla(a1, a2))

a3 = [int]
a4 = [1]
print(mezcla(a3, a4))
print(mezcla(a4, a3))

a5 = [1, 2, 3]
a6 = [-10, -9, -8]

print(mezcla(a6, a5))
