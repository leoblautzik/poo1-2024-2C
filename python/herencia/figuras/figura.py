"""Ejercicio tipo parcial"""

from abc import ABCMeta


class Figura(metaclass=ABCMeta):

    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    # __lt__ less than <
    #
    # __gt__ greater than >
    #
    # __eq__ equal to ==

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
