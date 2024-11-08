class EspectadoresPorEvento:

    def __init__(self):
        # self.__puertas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # self.__puertas = [0 for _ in range(15)]
        self.__puertas = [0] * 15
        self.__cantidad_total_espectadores = 0

    def ingresar_espectadores_por_la_puerta(self, puerta, espectadores):
        self.__puertas[puerta - 1] += espectadores
        self.__cantidad_total_espectadores += espectadores

    # def get_espectadores_que_ingresaron_por_la_puerta(self, puerta):
    #     return self.__puertas[puerta - 1]
    #
    # def get_cantidad_total_de_espectadores(self):
    #     return self.__cantidad_total_espectadores

    def __str__(self) -> str:
        s = "CTE:" + str(self.__cantidad_total_espectadores) + "\n"
        for i in range(14):
            s += "Puerta " + str(i + 1) + ": " + str(self.__puertas[i]) + ", "
        s += "Puerta " + str(15) + ": " + str(self.__puertas[14])
        return "\n" + s
