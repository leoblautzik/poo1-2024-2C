"""Clase Soldado que extiende de Unidad
Los soldados pueden atacar cuerpo a cuerpo a otras unidades si tienen suficiente energía. 
Cada ataque les consume 10 puntos de energía, y comienzan con 100. 
Restauran energía si reciben la ración de agua. 
Infligen un daño de 10 puntos y comienzan con 200 de salud
"""

from unidad import Unidad


class Soldado(Unidad):
    """Class soldado"""

    def __init__(self, posicion) -> None:
        super().__init__(10, 200, posicion)
        self.__energia = 100

    def puede_atacar(self, enemigo: Unidad) -> bool:
        return (
            not enemigo.esta_muerto()
            and not self.esta_muerto()
            and self != enemigo
            and self.__energia >= 10
            and self.distancia(enemigo) <= 1
        )

    def atacar(self, enemigo) -> None:
        if self.puede_atacar(enemigo):
            self.__energia -= 10
            self.infligir_danio(enemigo)
