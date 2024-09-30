"""Class Cuadrado"""

from rectangulo import Rectangulo


class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)
