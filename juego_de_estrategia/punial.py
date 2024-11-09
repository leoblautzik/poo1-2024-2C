"""Un punal aumenta la fuerza de los ataques en 3 puntos pero reduce la defensa tambien en
3 puntos por inutilizar la otra mano."""

from item import Item


class Punial(Item):

    def __init__(self, unidad) -> None:
        super().__init__(unidad.get_danio(), unidad.get_salud(), unidad.get_posicion())
        self.unidad = unidad

    def infligir_danio(self, oponente) -> None:
        oponente.sufrir_danio(self.unidad.get_danio() + 3)

    def sufrir_danio(self, danio) -> None:
        super().set_salud(super().get_salud() - (danio - 3))

    def puede_atacar(self, oponente) -> bool:
        return self.unidad.puede_atacar(oponente)

    def atacar(self, oponente):
        self.infligir_danio(oponente)
