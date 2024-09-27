"""Los Arqueros pueden atacar a una distancia de entre 2 y 5 respecto de su enemigo, 
   y si tienen suficientes flechas. 
   Comienzan con 20 flechas en su carcaj, y pueden recargar si reciben un paquete de seis flechas. 
   Infringen un daño de 5 puntos, y comienzan con 50 de salud
"""

from unidad import Unidad


class Arquero(Unidad):
    """Class Arquero"""

    def __init__(self, posicion):
        super().__init__(5, 50, posicion)
        self.__flechas = 20

    def get_flechas(self):
        """Devuelve las flechas que le quedan al arquero"""
        return self.__flechas

    def recargar_flechas(self):
        """Recarga el pack de 6 flechas"""
        self.__flechas += 6

    def puede_atacar(self, oponente: Unidad) -> bool:
        return (
            not oponente.esta_muerto()
            and not self.esta_muerto()
            and self != oponente
            and self.get_flechas() >= 1
            and self.distancia(oponente) <= 5
            and self.distancia(oponente) >= 1
        )

    def atacar(self, oponente: Unidad):
        if self.puede_atacar(oponente):
            self.__flechas -= 1
            # oponente.sufrir_danio(self)
            self.infligir_danio(oponente)
