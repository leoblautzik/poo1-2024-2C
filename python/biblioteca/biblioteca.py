"""Class Biblioteca con lista, enumerados y maps"""

from libro import Libro
from genero import Genero


class Biblioteca:

    def __init__(self):
        self.__libros = []

    def agregar_libro(self, titulo, autor, genero, paginas):
        """Agrega un libro a la biblioteca definido por su titulo,
        autor, genero literario y cantidad de paginas"""
        self.__libros.append(Libro(titulo, autor, genero, paginas))

    def cuantos_libros(self) -> int:
        """Devuelve la cantidad de libros en la biblioteca"""

        return len(self.__libros)

    def libro_en_posicion(self, posicion) -> str:
        """Devuelve el titulo del libro en la posicion que se pasa por parametro"""
        if posicion < 1 or posicion > len(self.__libros):
            raise ValueError("Posicion fuera de rango")

        return self.__libros[posicion - 1].get_titulo()

    def libro_ultima_posicion(self) -> str:
        """Devuelve el titulo del libro en la ultima posicion"""
        ultimo = self.cuantos_libros()

        return self.__libros[ultimo].get_titulo()

    def libro_con_mas_paginas(self) -> Libro:
        """Devuelve el libro con mas paginas"""
        maxilibro = self.__libros[0]
        for libro in self.__libros:
            if libro.get_paginas() > maxilibro.get_paginas():
                maxilibro = libro

        return maxilibro

    def cuantos_libros_del_autor(self, autor) -> int:
        """Devuelve la cantidas de libros del autor que hay en la biblioteca"""
        contador = 0
        for libro in self.__libros:
            if libro.get_autor() == autor:
                contador += 1

        return contador

    def libros_del_autor(self, autor) -> list[Libro]:
        """Devuelve ina lista con todos los libros del autor"""
        aux = []
        for libro in self.__libros:
            if libro.get_autor() == autor:
                aux.append(libro)
        return aux

    def libros_por_genero_literario(self):
        s = ""
        mapa = {}
        for libro in self.__libros:
            generos = mapa.keys()
            genero = libro.get_genero()

            if generos.__contains__(genero):
                lista = mapa[genero]
            else:
                lista = []

            lista.append(libro)
            mapa[genero] = lista

        print(type(mapa))
        generos = mapa.keys()
        for genero in generos:
            s += "\n" + str(genero) + "\n"
            s += "-------------\n"
            libros = mapa[genero]
            for libro in libros:
                s += str(libro) + "\n"

        return s


elNegrito = Biblioteca()

elNegrito.agregar_libro("Moby-Dick", "Melville", Genero.AVENTURA, 823)
elNegrito.agregar_libro("Crepusculo", "Mayer", Genero.NOVELA, 789)
elNegrito.agregar_libro("Crepusculo - Nueva Luna", "Mayer", Genero.NOVELA, 689)
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

principito = Libro("El Principito", "Antoine de Saint-Exupéry", Genero.INFANTILES, 96)
print(principito)
print(elNegrito.libros_por_genero_literario())
print(elNegrito.cuantos_libros_del_autor("Mayer"))
print(elNegrito.libros_del_autor("Mayer"))
