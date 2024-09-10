"""Class Corona Circular"""

from src import circulo
from src import punto


class CooronaCircular:
    """
    Modela una Corona Circular
    pre: ambos radios son mayores que cero y r_g es mayor que r
    """

    def __init__(self, r, r_g, x_c, y_c):
        if r_g <= r:
            raise ValueError("El radio grande dbe ser mayor al chico")
        self.__centro = punto.Punto(x_c, y_c)
        self.__circulo_grande = circulo.Circulo(r_g, x_c, y_c)
        self.__circulo_chico = circulo.Circulo(r, x_c, y_c)

    def area(self):
        """pos: Devuelve el area de la corona circular"""
        return self.__circulo_grande.get_area() - self.__circulo_chico.get_area()

    def perimetro(self):
        """pos: Devuelve el perímetro de la corona circular"""
        return (
            self.__circulo_chico.get_perimetro() + self.__circulo_grande.get_perimetro()
        )

    def desplazar(self, en_x, en_y):
        """
        Desplaza la corona circular
        pos: La corona queda en su nueva posicion
        """
        self.__centro.desplazar(en_x, en_y)
