"""Implementar una función que reciba como parámetro un arreglo de enteros y 
muestre por pantalla cuántas veces se repite cada uno. 
El arreglo no está ordenado. Se garantiza que los valores del arreglo están comprendidos 
entre 0 y 100
"""


def frecuencias(a) -> str:
    s = ""
    f = []
    for i in range(101):
        f.append(0)

    for value in a:
        f[value] += 1

    for i in range(101):
        if f[i] != 0:
            s = s + str(i) + ":\t" + str(f[i]) + "\n"

    return s


def swap(a, b):
    aux = a
    a = b
    b = aux


# main
v = [23, 23, 0, 1, 1, 1, 1, 45, 7, 7, 8, 1, 1, 89, 9, 9, 9, 9, 9, 9, 9, 100]
print(v)
print(frecuencias(v))
x = 5
y = 10
print("x = ", x)
print("y = ", y)
swap(x, y)
print("x = ", x)
print("y = ", y)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
swap(l1, l2)
print(l1, l2)
