"""Class Circulo"""

import math
from src import punto


class Circulo:
    """Modela un circulo a partir de su radio y su centro"""

    def __init__(self, radio: float = 1, x_centro: float = 0.0, y_centro: float = 0.0):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__diametro = radio * 2
        # self.__xcentro = x_centro
        # self.__y_centro = y_centro
        self.__centro = punto.Punto(x_centro, y_centro)

    def get_centro(self):
        """Devuelve un Punto que es el centro del circulo"""
        return self.__centro

    def get_radio(self):
        """Devuelve el radio del circulo"""
        return self.__diametro / 2

    def set_radio(self, r):
        """Establece el radio en el valor r"""
        self.set_diametro(r * 2)

    def get_diametro(self):
        """Devuelve el diametro del circulo"""

        return self.__diametro

    def set_diametro(self, d):
        """Establece el diametro en el valor d pasado como parametro"""
        if d <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__diametro = d

    def get_perimetro(self):
        """Devuelve la logitud de circunferencia
        del circulo o su perimetro"""
        return math.pi * self.get_diametro()

    def set_perimetro(self, p):
        """Establece el perimetro en el valor de p"""
        self.set_radio(p / (2 * math.pi))

    def get_area(self):
        """Devuelve el area del circulo"""
        return math.pi * math.pow(self.get_radio(), 2)

    def set_area(self, a):
        """Establece el area en el valor a"""
        self.set_radio(math.sqrt(a / math.pi))

    def desplazar(self, en_x, en_y):
        """Desplaza el circulo"""
        self.__centro.desplazar(en_x, en_y)
