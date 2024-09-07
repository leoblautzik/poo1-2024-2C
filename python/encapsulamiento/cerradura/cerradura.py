"""Modelamos una derradura de combinacion"""


class Cerradura:

    #    public Cerradura(int claveDeApertura,int cantidadDeFallosConsecutivosQueLaBloquean)
    def __init__(self, clave_de_apertura, cant_fallos_bloq):
        self.__key = clave_de_apertura
        self.__fallos_consecutivos = cant_fallos_bloq
        self.__fallos = 0
        self.__esta_abierta = True
        self.__esta_bloqueada = False
        self.__cant_aperturas_exitosas = 0

    def abrir(self, clave):
        """pre: esta cerrada y no esta bloqueada
        pos: se abre la cerradura
        """
        if not self.__esta_bloqueada:
            if clave == self.__key:
                self.__esta_abierta = True
                self.__cant_aperturas_exitosas += 1
                self.__fallos = 0
            else:
                self.__fallos += 1
                if self.__fallos == self.__fallos_consecutivos:
                    self.__esta_bloqueada = True


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
