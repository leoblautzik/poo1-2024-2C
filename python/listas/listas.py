"""Ejercicios con listas en python"""


def eliminar_duplicados(lista):
    """Escribe el método eliminarDuplicados, que recibe una lista de enteros y devuelve una
    nueva lista con los mismos elementos pero eliminando los repetidos.
    Por ejemplo, si la lista de entrada es: [1, 2, 2, 1, 4, 2, 4, 3],
    la salida sería: [1, 2, 4, 3].
    """
    aux = []

    for x in lista:
        if not x in aux:
            aux.append(x)

    return aux


def invertir_lista(lista):
    """Escriba un método que reciba una lista de enteros y la devuelva invertida.
    Por ejemplo si recibe la lista [1, 2, 3, 4, 5] devolverá la lista [5, 4, 3, 2, 1].
    """
    aux = []

    # for i in range(len(lista) - 1, -1, -1):
    #     aux.append(lista[i])

    # for x in reversed(lista):
    #     aux.append(x)

    for i in range(len(lista)):
        aux.append(lista[len(lista) - 1 - i])
    return aux


def contiene_suma_de_dos(lista):
    # for i in range(len(lista)):
    #     for j in range(len(lista)):
    #         if (i != j) and (lista[i] + lista[j] in lista):
    #             return True
    # for x in lista:
    #     for y in lista:
    #         if lista.index(x) != lista.index(y) and x + y in lista:
    #             return True

    for i, x in enumerate(lista):
        for j, y in enumerate(lista):
            if (i != j) and (x + y in lista):
                return True

    return False


def es_sublista_de(lista1, lista2):
    """Escriba un método que devuelva true si una lista de enteros es sublista de otra.
    Por ejemplo: si tenemos las listas
    L1 = [22, 14, 6] y
    L2 = [39, 41, 17, 22, 14, 6, 3, 11, 73, 81]
    entonces el método devolverá true porque L1 es una sublista de L2.
    Pero si tenemos otra lista
    L3 = [39, 41, 22, 17, 14, 3, 11, 73, 6, 81],


    vemos que L1 no es sublista de L3 por lo que el método llamado con L1 y L3 debe devolver false.
    """

    for i in range(len(lista2) - len(lista1)):
        if lista2[i : len(lista1) + i] == lista1:
            return True
    return False


# l = [1, 2, 2, 1, 4, 2, 4, 3]
#
# print("Contiene", l[1:5] in l)
# sindu = eliminar_duplicados(l)
# print(sindu)

# print(invertir_lista(l))

# ll = [10, -1, 7, 25, 98]
# lll = [1, 2]
# l4 = []
# l5 = [1]
# print(contiene_suma_de_dos(l))
# print(contiene_suma_de_dos(ll))
# print(contiene_suma_de_dos(lll))
# print(contiene_suma_de_dos(l4))
# print(contiene_suma_de_dos(l5))
l1 = [22, 14, 6]
l2 = [39, 41, 17, 22, 14, 6, 3, 11, 73, 81]
l3 = [39, 41, 22, 17, 14, 3, 11, 73, 6, 81]

print(es_sublista_de(l1, l2))
print(es_sublista_de(l1, l3))
