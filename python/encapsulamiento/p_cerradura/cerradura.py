"""Modelamos una cerradura de combinacion"""


class Cerradura:
    """class Cerradura de combinacion"""

    def __init__(self, clave_de_apertura, fallos_bloqueo):
        self.__key = clave_de_apertura
        self.__fallos_bloqueo = fallos_bloqueo
        self.__fallos = 0
        self.__fallos_consecutivos = 0
        self.__abierta = True
        self.__bloqueada = False
        self.__aperturas_exitosas = 0

    def abrir(self, clave):
        """pre: esta cerrada y no esta bloqueada
        pos: se abre la cerradura
        """
        if not self.esta_abierta():
            if not self.fue_bloqueada():
                if clave == self.__key:
                    self.__abierta = True
                    self.__aperturas_exitosas += 1
                    self.__fallos_consecutivos = 0
                else:
                    self.__fallos += 1
                    self.__fallos_consecutivos += 1
                    if self.__fallos_consecutivos == self.__fallos_bloqueo:
                        self.__bloqueada = True

    def cerrar(self):
        self.__abierta = False

    def esta_abierta(self) -> bool:
        return self.__abierta

    def esta_cerrada(self) -> bool:
        return not self.esta_abierta()

    def fue_bloqueada(self) -> bool:
        return self.__bloqueada

    def contar_aperturas_exitosas(self) -> int:
        return self.__aperturas_exitosas

    def contar_aperturas_fallidas(self) -> int:
        return self.__fallos


#
#     public boolean abrir(int clave)
#
#     public void cerrar()
#
#     public boolean estaAbierta()
#
#     public boolean estaCerrada()
#
#     public boolean fueBloqueada()
#
#     public int contarAperturasExitosas()
#
#     public int contarAperturasFallidas()
#
# }
