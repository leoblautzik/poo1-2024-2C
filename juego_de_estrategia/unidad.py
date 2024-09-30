"""Juego Estrategia"""

from abc import ABCMeta, abstractmethod


class Unidad(metaclass=ABCMeta):
    """Clase abstracta Unidaad"""

    def __init__(self, danio, salud, posicion) -> None:
        self.__posicion = posicion
        self.__danio = danio
        self.__salud = salud

    # @abstractmethod
    # def atacar(self, oponente) -> None:
    #     """self ataca al oponente"""

    def atacar(self, oponente) -> None:
        if self.puede_atacar(oponente):
            self.infligir_danio(oponente)

    @abstractmethod
    def puede_atacar(self, oponente) -> bool:
        """Devuelve true o false si self puede atacar o no a
        su oponente"""

    def get_danio(self) -> float:
        """devualve el danio"""

        return self.__danio

    def get_salud(self) -> float:
        """Devuelve la salud"""

        return self.__salud

    def set_salud(self, salud) -> None:
        """Establece el nuevo valor para la salud"""
        self.__salud = salud

    def get_posicion(self) -> float:
        """Devuelve la posicion"""

        return self.__posicion

    def distancia(self, oponente) -> float:
        """devuelve la distancia entre self y su oponente"""

        return abs(self.__posicion - oponente.get_posicion())

    def esta_muerto(self) -> bool:
        """Devuelve True o False segun sea el estado de salud de la unidad"""
        return self.get_salud() <= 0

    def infligir_danio(self, oponente) -> None:
        """El oponente recibe el danio inflingido por self"""
        oponente.set_salud(oponente.get_salud() - self.get_danio())

    def sufrir_danio(self, oponente) -> None:
        """self recibe el danio inflingido por el oponente"""
        self.set_salud(self.get_salud() - oponente.get_danio())

    def desplazarse(self, nueva_posicion):
        """la unidad se desplaza a la nueva posicion"""
        self.__posicion = nueva_posicion
