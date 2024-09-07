"""class TarjetaBaja"""


class TarjetaBaja():

    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
        self.__viajes_en_colectivo = 0
        self.__viajes_en_subte = 0

    def obtener_saldo(self):
        return self.__saldo

    def pagar_viaje_en_colectivo(self):
        if self.__hay_saldo_para_un_bondi():
            self.__saldo -= 21.50
            self.__viajes_en_colectivo += 1

    def pagar_viaje_en_subte(self):
        if self.__hay_saldo_para_un_subte():
            self.__saldo -= 19.50
            self.__viajes_en_subte += 1

    def contar_viajes(self):
        return self.__viajes_en_colectivo + self.__viajes_en_subte

    def contar_viajes_en_colectivo(self):
        return self.__viajes_en_colectivo

    def contar_viajes_en_subte(self):
        return self.__viajes_en_subte

    def __hay_saldo_para_un_bondi(self):
        return self.__saldo >= 21.50

    def __hay_saldo_para_un_subte(self):
        return self.__saldo >= 19.50
