class PuertaInexistenteException(Exception):
    pass


class EspectadoresPorEvento:
    def __init__(self) -> None:
        self.__puertas = [0] * 15
        self.__cantidad_total_espectadores = 0

    def ingresar_espectadores_por_puerta(self, puerta, ce):
        self.__puertas[puerta - 1] += ce
        self.__cantidad_total_espectadores += ce

    def __str__(self):
        s = "CTE: " + str(self.__cantidad_total_espectadores) + "  "
        for i in range(15):
            s += "(" + str(i + 1) + ")" + str(self.__puertas[i]) + "\t"
        return s


class GestionEventos:

    def __init__(self):
        self.__estadio = {}

    def cargar_eventos(self, entrada):
        with open(entrada, "r", encoding="UTF-8") as fr:
            for cada_linea in fr:
                try:
                    datos = cada_linea.strip().split(",")
                    partido = datos[0]
                    puerta = int(datos[1])
                    if puerta < 1 or puerta > 15:
                        raise PuertaInexistenteException
                    ce = int(datos[2])
                    epe = self.__estadio.get(partido, EspectadoresPorEvento())
                    epe.ingresar_espectadores_por_puerta(puerta, ce)
                    self.__estadio.update({partido: epe})

                except ValueError:
                    print("Valores no numericos")
                except PuertaInexistenteException:
                    print("Puerta mala")

    def escribir_espectadores_por_evento(self, salida):
        with open(salida, "w", encoding="utf-8") as fw:
            for partido, epe in self.__estadio.items():
                fw.write(partido + "\n")
                fw.write(str(epe) + "\n")


# main

ge = GestionEventos()
while True:
    try:
        entrada = input("Ingrese el archivo de datos: ")
        ge.cargar_eventos(entrada)
        break
    except FileNotFoundError:
        print("No se encuentra el archivo, intente nuevamente")

ge.escribir_espectadores_por_evento("espectadores_por_evento.txt")
