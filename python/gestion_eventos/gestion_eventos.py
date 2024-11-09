"""Gestion eventos"""

import os
from espectadores_por_evento import EspectadoresPorEvento


class PuertaFueraDeRangoException(Exception):
    pass


class EspectadoresNulosException(Exception):
    pass


class GestionEventos:
    """class GestionEventos"""

    def __init__(self):
        self.__estadio = {}

    def cargar_eventos(self, archivo):
        """carga el diccionario estadio con los datos del archivo"""
        with open(archivo, "r", encoding="utf-8") as ev:
            for linea in ev:
                try:
                    datos = linea.split(",")
                    cod_ev = datos[0]
                    puerta = int(datos[1])
                    if puerta < 1 or puerta > 15:
                        raise PuertaFueraDeRangoException
                    ce = int(datos[2])
                    if ce <= 0:
                        raise EspectadoresNulosException
                    epe = self.__estadio.get(cod_ev, EspectadoresPorEvento())
                    epe.ingresar_espectadores_por_la_puerta(puerta, ce)
                    self.__estadio.update({cod_ev: epe})
                except PuertaFueraDeRangoException:
                    print("Puerta fuera de rango")
                except ValueError:
                    print("Alguno de los valores no es un entero")
                except EspectadoresNulosException:
                    print("La cantidad de espectadores debe mayor a cero")

    def gener_epe(self, archivo):
        """Escribe en el archivo los datos de cada evento"""
        with open(archivo, "w", encoding="utf-8") as fw:
            for cod_ev, epe in self.__estadio.items():
                fw.write(cod_ev)
                fw.write(str(epe) + "\n")


# main
ge = GestionEventos()
while True:
    try:
        file = input("Ingrese el nombre del archivo de datos: ")
        ge.cargar_eventos(file)
        break
    except FileNotFoundError:
        print("No se encuentra el archivo, intenete nuevamente...")
        for f in os.listdir("."):  # Lista de archivos y directorios
            print(f)

ge.gener_epe("espectadores.txt")
