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
        print(
            "Soy un punto de coordenadas: x =",
            self.get_x(),
            " y =",
            self.get_y(),
        )

    def esta_sobre_eje_x(self) -> bool:
        """Devuelve True o False segun el punto pertenezca o no al eje X"""
        return self.get_y() == 0

    def esta_sobre_eje_y(self) -> bool:
        """Devuelve True o False segun el punto pertenezca o no al eje Y"""
        return self.get_x() == 0

    def es_el_origen(self) -> bool:
        """Devuelve True o False segun el punto sea o no el origen
        de coordenadas"""
        return self.esta_sobre_eje_y() and self.esta_sobre_eje_x()

    def distancia_al_origen(self) -> float:
        """Devuelve la distancia desde el punto al origen de coordenadas"""
        return math.sqrt(pow(self.__x, 2) + pow(self.__y, 2))

    def distancia(self, otro) -> float:
        """Devuelve la distacia entre self y otro punto que se pasa por parametro"""
        return math.sqrt(
            pow(self.__x - otro.get_x(), 2) + pow(self.__y - otro.get_y(), 2)
        )

    def desplazar_en_x(self, d_en_x):
        """Desplaza el punto en la direccion de x lo que indique el parametro d_en_x"""
        self.__x = self.__x + d_en_x

    def desplazar_en_y(self, d_en_y):
        """Desplaza el punto en la direccion de y lo que indique el parametro d_en_y"""
        self.__y = self.__y + d_en_y

    def desplazar(self, d_en_x, d_en_y):
        """Desplaza el punto en la direccion de x lo que indique el parametro d_en_x
        y desplaza el punto en la direccion de y lo que indique el parametro d_en_y"""
        self.desplazar_en_x(d_en_x)
        self.desplazar_en_y(d_en_y)

    def __str__(self):
        """Devuelve un string con las coordenadas
        del punto en forma de par ordenado"""
        return "( " + str(self.get_x()) + ", " + str(self.get_y()) + " )"

    def __eq__(self, other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()


# p1 = Punto(4, 6)
# p2 = Punto(4, 6)
# p1.mostrar_punto()
# p2.mostrar_punto()
# print(p1)
# print(p2)
# print(p1 == p2)
