"""Tipo enumerado para los libros de la biblioteca"""

from enum import Enum


class Genero(Enum):
    """Genero literario"""

    POESIA = 1
    NOVELA = 2
    CIENCIA_FICCION = 3
    AVENTURA = 4
    TERROR = 5
    HISTORIA = 6
    INFANTILES = 7

    def __str__(self):
        return self.name
