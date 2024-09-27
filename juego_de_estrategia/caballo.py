"""Class caballo que se pone rebelde"""

from hidratable import Hidratable


class Caballo(Hidratable):

    def __init__(self):
        self.__ataques = 0
        self.__rebelde = False

    def incrementar_ataques(self):
        if self.__ataques < 3:
            self.__ataques += 1
        if self.__ataques >= 3:
            self.__rebelde = True

    def __calmar(self):
        self.__rebelde = False
        self.__ataques = 0

    def beber_agua(self):
        self.__calmar()

    def esta_rebelde(self):
        return self.__rebelde
