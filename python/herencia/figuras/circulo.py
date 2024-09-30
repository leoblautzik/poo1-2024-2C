"""Circulo"""

from elipse import Elipse


class Circulo(Elipse):

    def __init__(self, radio):
        super().__init__(radio, radio)
