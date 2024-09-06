"""Class cubo dado cubito, etc"""

import math


class Cubo:
    """class Cubo"""

    def __init__(self, lado):
        """
        pre : longitudLado es un valor mayor a 0.
        post: inicializa el cubo a partir de la longitud de lado dada
        """
        self.set_lado(lado)

    def get_lado(self):
        """Devuelve el valor del lado o arista del cubo"""
        return self.__lado

    def set_lado(self, lado):
        """Cambia el valor de la arista del cubo al valor del parametro lado"""
        if lado <= 0:
            raise ValueError("El valor del lado debe ser positivo")
        self.__lado = lado

    def get_area_cara(self):
        """Devuelve el area de cada una de las caras del cubo"""
        return pow(self.__lado, 2)

    def set_area(self, a):
        """Cambia el valor del lado del cubo para que cambie el area de la cara
        al valor pasado por parametro"""
        if a <= 0:
            raise ValueError("El valor del área debe ser positivo")
        self.set_lado(math.sqrt(a))

    def get_volumen(self):
        """Devuelve el volumen del cubo"""
        return pow(self.get_lado(), 3)

    def set_volumen(self, v):
        """Cambia el valor del lado del cubo para que cambie el volumen del cubo
        al valor pasado por parametro"""
        if v <= 0:
            raise ValueError("El valor del volumen debe ser positivo")
        self.set_lado(math.cbrt(v))
