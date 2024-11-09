"""Lancero"""

from unidad import Unidad


class Lancero(Unidad):

    def __init__(self, posicion):
        super().__init__(25, 150, posicion)

    def puede_atacar(self, oponente: Unidad) -> bool:
        """Comentario"""
        return (
            not oponente.esta_muerto()
            and not self.esta_muerto()
            and not self is oponente
            and self.distancia(oponente) <= 2
            and self.distancia(oponente) >= 1
        )

    def atacar(self, oponente: Unidad):
        if self.puede_atacar(oponente):
            oponente.sufrir_danio(self.get_danio())
