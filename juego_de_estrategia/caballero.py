"""Class caballero que tiene un caballo"""

from unidad import Unidad
from caballo import Caballo


class Caballero(Unidad):
    """Clas Caballero con un caballo"""

    def __init__(self, posicion) -> None:
        super().__init__(50, 200, posicion)
        self.__caballo = Caballo()

    def atacar(self, oponente) -> None:
        super().atacar(oponente)
        self.__caballo.incrementar_ataques()

    def puede_atacar(self, oponente: Unidad) -> bool:

        return (
            not oponente.esta_muerto()
            and not self.esta_muerto()
            and self != oponente
            and not self.__caballo.esta_rebelde()
            and self.distancia(oponente) >= 1
            and self.distancia(oponente) <= 2
        )

    def calmar_caballo(self):
        """Le da de beber al aballo para calmarlo y poder atacar"""
        self.__caballo.beber_agua()

    def get_caballo_rebelde(self):
        return self.__caballo.esta_rebelde()
