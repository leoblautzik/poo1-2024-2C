"""Class libro con las responsabilidades necesarias en la biblioteca"""

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

    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_genero(self) -> Genero:
        return self.__genero

    def get_paginas(self) -> int:
        return self.__paginas

    def __str__(self) -> str:
        return (
            "Titulo: "
            + self.__titulo
            + " Autor: "
            + self.__autor
            + " Genero: "
            + str(self.__genero)
            + " Paginas: "
            + str(self.__paginas)
        )

    def __eq__(self, other) -> bool:
        return (
            self.__titulo == other.get_titulo()
            and self.__autor == other.get_autor()
            and self.get_genero() == other.get_genero()
            and self.get_paginas() == other.get_paginas()
        )
