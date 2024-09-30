"""Elipse"""

import math
from figura import Figura


class Elipse(Figura):

    def __init__(self, radio_mayor, radio_menor):
        super().__init__(math.pi * radio_mayor * radio_menor)
