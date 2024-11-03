"""Biblioteca con lista y mapa"""

from typing import List
from libro import Libro
from genero import Genero


class Biblioteca:

    def __init__(self):
        self.__libros = []

    def cuantos_libros(self):
        return len(self.__libros)

    def agregar_libro(self, titulo, autor, genero, paginas):
        l = Libro(titulo, autor, genero, paginas)
        self.__libros.append(l)

    def libro_en_la_posicion(self, posicion):
        if posicion < 1 or posicion > self.cuantos_libros():
            raise ValueError("Posicion fuera de la biblioteca")
        return self.__libros[posicion - 1]

    def libro_ultima_posicion(self):
        return self.libro_en_la_posicion(self.cuantos_libros())

    def libro_mas_paginas(self) -> Libro:
        maxilibro = self.__libros[0]
        for libro in self.__libros:
            if libro.get_paginas() > maxilibro.get_paginas():
                maxilibro = libro

        return maxilibro

    def cuantos_libros_autor(self, autor):
        contador = 0
        for libro in self.__libros:
            if libro.get_autor() == autor:
                contador += 1

        return contador

    def libros_autor(self, autor) -> List[Libro]:
        libros_del_autor = []
        for libro in self.__libros:
            if libro.get_autor() == autor:
                libros_del_autor.append(libro)

        return libros_del_autor

    def __str__(self):
        s = "Biblioteca \n"
        for libro in self.__libros:
            s = s + str(libro) + "\n"
        return s

    def ordenar_biblioteca(self):
        self.__libros.sort()

    def libros_por_genero(self):

        libros_genero = {}

        for libro in self.__libros:
            claves = libros_genero.keys()
            genero = libro.get_genero()
            if genero in claves:
                lista = libros_genero[genero]
            else:
                lista = []
            lista.append(libro)
            libros_genero[genero] = lista

        # return libros_genero

        claves = libros_genero.keys()
        for genero in claves:
            print(genero)
            lista = libros_genero[genero]
            for libro in lista:
                print(libro)


# --------------------------------------------------

elNegrito = Biblioteca()

elNegrito.agregar_libro("Moby-Dick", "Melville", Genero.AVENTURA, 823)
elNegrito.agregar_libro("Crepusculo", "Mayer", Genero.NOVELA, 789)
elNegrito.agregar_libro("Crepusculo - Nueva Luna", "Mayer", Genero.NOVELA, 689)
elNegrito.agregar_libro(
    "Cien años de soledad", "Gabriel García Márquez", Genero.NOVELA, 400
)
elNegrito.agregar_libro(
    "Cien años de soledad", "Gabriel García Márquez", Genero.NOVELA, 400
)
elNegrito.agregar_libro(
    "El ingenioso hidalgo Don Quijote de la Mancha",
    "Miguel de Cervantes",
    Genero.NOVELA,
    900,
)
elNegrito.agregar_libro(
    "Crónicas de una muerte anunciada", "Gabriel García Márquez", Genero.NOVELA, 120
)
elNegrito.agregar_libro(
    "Harry Potter y la piedra filosofal", "J.K. Rowling", Genero.AVENTURA, 309
)
elNegrito.agregar_libro(
    "El Principito", "Antoine de Saint-Exupéry", Genero.INFANTILES, 96
)

# print(elNegrito.libro_mas_paginas())
# print(elNegrito.libros_autor("Mayer"))
# elNegrito.ordenar_biblioteca()
# print(elNegrito)
elNegrito.libros_por_genero()
