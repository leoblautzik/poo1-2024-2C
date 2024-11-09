"""Empleados del sector"""


class SectorFueraDeRangoException(Exception):
    pass


class Empleado:

    def __init__(self, sector, legajo, apenom, anti):
        self.__sector = sector
        self.__legajo = legajo
        self.__apenom = apenom
        self.__anti = anti

    def __str__(self):
        return str(self.__legajo) + ", " + self.__apenom + ", " + str(self.__anti)


class EmpleadosDelSector:

    def __init__(self):
        self.__eps = {}

    def leer_personal(self):
        with open("personal.csv", "r", encoding="utf-8") as fr:
            for linea in fr:
                sector = 0
                try:
                    datos = linea.split(",")
                    sector = int(datos[0])
                    if sector < 100 or sector > 300:
                        raise SectorFueraDeRangoException(
                            "Sector con valor " + str(sector)
                        )
                    legajo = int(datos[1])
                    apenom = datos[2]
                    anti = int(datos[3])
                    e = Empleado(sector, legajo, apenom, anti)
                    l = self.__eps.get(sector, [])
                    l.append(e)
                    self.__eps.update({sector: l})

                except ValueError:
                    print("Valores incorrectos")
                except SectorFueraDeRangoException:
                    print("Sector " + str(sector) + " incorrecto")

    def escribir_eps(self):
        with open("empleados_por_sector.txt", "w", encoding="utf-8") as fw:

            for sector, lista_e in self.__eps.items():
                fw.write(str(sector) + "\n")
                for e in lista_e:
                    fw.write(str(e) + "\n")


# main

eds = EmpleadosDelSector()

eds.leer_personal()
eds.escribir_eps()
