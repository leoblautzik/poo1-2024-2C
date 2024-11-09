from enum import Enum


class Genero(Enum):
    INFANTILES = 1
    POESIA = 2
    CIENCIA_FICCION = 3
    AVENTURA = 4
    NOVELA = 5
    TERROR = 6
    HISTORIA = 7

    def __str__(self):
        return self.name
