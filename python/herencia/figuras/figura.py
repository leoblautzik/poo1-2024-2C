"""Ejercicio tipo parcial"""

from abc import ABCMeta


class Figura(metaclass=ABCMeta):
    """Clase abstracta Figura"""

    def __init__(self, area: float):
        self.__area = area

    def get_area(self) -> float:
        """Devuelve el area de la figura"""
        return self.__area

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()

    def __str__(self) -> str:
        return type(self).__name__ + ", Area: " + str(self.get_area())
