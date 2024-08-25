"""Modela un punto en el plano"""

import math


class Punto:
    """Modela un punto en el plano de coordenadas x e y"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        """Retorna la coordenada x del punto"""
        return self.__x

    def get_y(self):
        """Retorna la coordenada y del punto"""
        return self.__y

    def mostrar_punto(self):
        """Muestra las coordenadas del Punto"""
        print("(", self.get_x(), ",", self.get_y(), ")")

    def string(self):
        """Devuelve un string con las coordenadas
        del punto en forma de par ordenado"""
        return "( " + str(self.get_x()) + ", " + str(self.get_y()) + " )"

    def distancia_al_origen(self):
        """Devuelve la distancia desde el punto al origen de coordenadas"""
        return math.sqrt(pow(self.__x, 2) + pow(self.__y, 2))

    def distancia_entre_dos_puntos(self, otro):
        """Devuelve la distacia entre self y otro punto que se pasa por parametro"""
        return math.sqrt(
            pow(self.__x - otro.get_x(), 2) + pow(self.__y - otro.get_y(), 2)
        )


p1 = Punto(4, 6)
p1.mostrar_punto()
print(p1.string())
