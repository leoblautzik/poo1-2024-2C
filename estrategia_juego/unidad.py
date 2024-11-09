"""Clase abstracta Unidad"""

from abc import ABCMeta, abstractmethod


class Unidad(metaclass=ABCMeta):
    """Clase abstracta Unidaad"""

    def __init__(self, danio, salud, posicion) -> None:
        self.__danio = danio
        self.__salud = salud
        self.__posicion = posicion

    @abstractmethod
    def puede_atacar(self, enemigo) -> bool:
        """Metodo abstracto puede_atacar"""

    @abstractmethod
    def atacar(self, enemigo) -> None:
        """Metodo abstracto atacar"""

    def get_salud(self):
        return self.__salud

    def set_salud(self, nueva_salud):
        self.__salud = nueva_salud

    def get_posicion(self):
        return self.__posicion

    def desplazarse(self, nueva_posicion):
        self.__posicion = nueva_posicion

    def get_danio(self):
        return self.__danio

    def esta_muerto(self) -> bool:
        return self.__salud <= 0

    def distancia(self, enemigo):
        return abs(self.__posicion - enemigo.get_posicion())

    def infligir_danio(self, enemigo) -> None:
        enemigo.set_salud(enemigo.get_salud() - self.get_danio())
