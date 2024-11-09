"""Class Soldado"""

from unidad import Unidad
from hidratable import Hidratable
from punial import Punial


class Soldado(Unidad, Hidratable):
    """class Soldado que extiende Unidad"""

    def __init__(self, posicion) -> None:
        super().__init__(10, 200, posicion)
        self.__energia = 100

    def get_energia(self):
        """Devuelve la energía actual del Soldado"""
        return self.__energia

    def atacar(self, oponente: Unidad):
        if self.puede_atacar(oponente):
            oponente.sufrir_danio(self.get_danio())
            self.__energia -= 10

    def puede_atacar(self, oponente: Unidad) -> bool:
        """Comentario"""
        return (
            not oponente.esta_muerto()
            and not self.esta_muerto()
            and not self is oponente
            and self.get_energia() >= 10
            and self.distancia(oponente) <= 1
        )

    def beber_agua(self) -> None:
        self.__energia = 100

    def __eq__(self, other) -> bool:
        return (
            self.get_danio() == other.get_danio()
            and self.get_energia() == other.get_energia()
            and self.get_salud() == other.get_salud()
            and self.get_posicion() == other.get_posicion()
        )

    def __str__(self):
        return (
            "Soldado en la posicion: "
            + str(self.get_posicion())
            + ", con energía de: "
            + str(self.get_energia())
            + " y una salud de "
            + str(self.get_salud())
        )


s1 = Soldado(1)
print(s1.get_danio())
s2 = Soldado(2)
s1 = Punial(s1)
print(s1.get_danio())
