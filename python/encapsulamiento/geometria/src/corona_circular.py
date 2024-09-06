"""Class Corona Circular"""

from src import circulo


class CooronaCircular:
    """Modela una Corona Circular"""

    def __init__(self, radio_interior, radio_exterior, x_centro, y_centro):
        self.__circulo_grande = circulo.Circulo(radio_exterior, x_centro, y_centro)
        self.__circulo_chico = circulo.Circulo(radio_interior, x_centro, y_centro)

    def get_centro(self):
        """Devuelve un Punto que es el centro de la corona circular"""
        return self.__circulo_grande.get_centro()

    def get_area(self):
        """Devuelve el area de la corona circular"""
        return self.__circulo_grande.get_area() - self.__circulo_chico.get_area()
