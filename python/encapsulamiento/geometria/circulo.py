"""Class Circulo"""

import math
import punto


class Circulo:
    """Modela un circulo a partir de su radio y su centro"""

    def __init__(self, radio, x_centro, y_centro):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = radio
        self.__centro = punto.Punto(x_centro, y_centro)

    def get_centro(self):
        """Devuelve un Punto que es el centro del circulo"""
        return self.__centro

    def get_radio(self):
        """Devuelve el radio del circulo"""
        return self.__radio

    def get_diametro(self):
        """Devuelve el diametro del circulo"""
        return 2 * self.get_radio()

    def get_perimetro(self):
        """Devuelve la logitud de circunferencia
        del circulo o su perimetro"""
        return math.pi * self.get_diametro()

    def get_area(self):
        """Devuelve el area del circulo"""
        return math.pi * math.pow(self.get_radio(), 2)
