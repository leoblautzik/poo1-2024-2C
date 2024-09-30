"""Class Triangulo"""

from figura import Figura


class Triangulo(Figura):

    def __init__(self, base, altura):
        super().__init__(base * altura / 2)
