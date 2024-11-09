"""Class Libro"""

from genero import Genero


class Libro:

    generos = [
        Genero.INFANTILES,
        Genero.POESIA,
        Genero.CIENCIA_FICCION,
        Genero.AVENTURA,
        Genero.NOVELA,
        Genero.HISTORIA,
    ]

    def __init__(self, titulo, autor, genero, paginas):
        self.__titulo = titulo
        self.__autor = autor

        self.__set_genero(genero)
        self.__paginas = paginas

    def __set_genero(self, genero):
        if not genero in self.generos:
            raise ValueError("Genero incorrecto")
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_genero(self):
        return self.__genero

    def get_paginas(self):
        return self.__paginas

    def __str__(self):
        return f"Titulo:{self.__titulo} Autor: {self.__autor} Genero: {self.__genero} Paginas {self.__paginas}"

    def __eq__(self, other):
        return (
            self.__titulo == other.get_titulo()
            and self.__autor == other.get_autor()
            and self.__genero == other.get_genero()
            and self.__paginas == other.get_paginas()
        )

    def __gt__(self, other):
        return self.__titulo > other.get_titulo()

    def __lt__(self, other):
        return self.__titulo < other.get_titulo()
