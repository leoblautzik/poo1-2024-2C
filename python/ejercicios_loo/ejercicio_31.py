"""Escribir una función que reciba un arreglo de enteros y 
devuelva la suma de los elementos que se encuentran en 
posiciones pares (incluido el elemento de la posición 0). 
Por ejemplo: Dado el arreglo [1, 2, 13 ,4, 8, 6] 
=> devuelve 22 (1+13+8)
"""


def suma_posiciones_pares(a):
    """Devuelve la suma de los elem en las pos pares"""
    # for (int i=0;i<len(a);i++)
    suma = 0
    for i in range(0, len(a), 2):
        suma += a[i]
    return suma


arreglo = [1, 2, 13, 4, 8, 6]
print(suma_posiciones_pares(arreglo))
