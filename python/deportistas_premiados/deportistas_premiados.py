"""Deportistas premiados"""

from os import write


class AnioIncorrectoException(Exception):
    pass


class Deportista:

    def __init__(self, deportista, anio, torneo):
        self.__deportista = deportista
        self.__anio = anio
        self.__torneo = torneo

    def __str__(self):
        return (
            self.__deportista + ": " + self.__torneo + ", En el año " + str(self.__anio)
        )


class DeportistasPremiados:

    def __init__(self) -> None:
        self.__dicci = {}

    def cargar_deportistas(self, archivo):
        with open(archivo, "r", encoding="utf-8") as fr:
            for cada_linea in fr:
                try:
                    datos = cada_linea.strip().split(",")
                    deportista = datos[0]
                    anio = int(datos[1])
                    if anio < 1877 or anio > 2024:
                        raise AnioIncorrectoException
                    torneo = datos[2]
                    lista = self.__dicci.get(anio, [])
                    lista.append(Deportista(deportista, anio, torneo))
                    self.__dicci.update({anio: lista})
                except ValueError:
                    print("Uno de los valores numericos es incorrecto")
                except AnioIncorrectoException:
                    print("Año invalido")

    def escribir_premios_por_anio(self, archivo):
        # ordenado = dict(sorted(self.__dicci.items()))
        # with open(archivo, "w", encoding="utf-8") as fw:
        #     for anio, lista in ordenado.items():
        #         fw.write(str(anio) + "\n")
        #         for d in lista:
        #             fw.write(str(d))

        with open(archivo, "w", encoding="utf-8") as fw:
            claves = sorted(self.__dicci.keys())
            for anio in claves:
                fw.write(str(anio) + "\n")
                lista = self.__dicci.get(anio, None)
                for d in lista:
                    fw.write(str(d) + "\n")


# main
dp = DeportistasPremiados()
while True:
    try:
        entrada = input("Ingrese el archivo de datos: ")
        dp.cargar_deportistas(entrada)
        break
    except FileNotFoundError:
        print("No se encuentra el archivo, intente nuevamente")

dp.escribir_premios_por_anio("premios.txt")
