"""Class RegistroDePersonas"""

from persona import Persona


class RegistroDePersonas:
    """class RegistroDePersonas"""

    def __init__(self) -> None:
        self.__personas = []

    def get_personas(self, archivo):
        """Carga los datos del archivo en la lista de personas"""
        with open(archivo, "r", encoding="utf-8") as fr:
            for cada_linea in fr:
                linea = cada_linea.replace("\n", "")
                datos = linea.split(",")
                try:
                    p = Persona(int(datos[0]), datos[1], int(datos[2]), datos[3])
                    self.__personas.append(p)
                except ValueError:
                    print("Dato incorrecto")

    def mostrar_personas(self):
        """Muestra por pantalla el contenido del atributo personas"""
        for p in self.__personas:
            print(p)

    def get_personas_mayores_que(self, edad):
        """Devuelve una lista con las personas mayores que una edad que se recibe por parametro"""
        pm = []
        for p in self.__personas:
            if p.get_edad() > edad:
                pm.append(p)

        return pm

    def escribir_personas(self, lista, nombre_archivo):
        """Escribe en disco con un nombre que se recibe por parametro,
        el contenido del parametro lista"""
        with open(nombre_archivo, "w", encoding="utf-8") as fw:
            for p in lista:
                fw.write(str(p) + "\n")

        fw.close()

    def cuantas_por_provincia(self):
        """genera el archivo "cuantas_por_provincia.txt" """
        dicc = {}

        for p in self.__personas:
            key = p.get_provincia()
            value = dicc.get(key, 0)
            value += 1
            dicc.update({key: value})

        with open("cuantos_por_rovincia.txt", "w", encoding="utf-8") as fw:
            for key, value in dicc.items():
                fw.write(key + ": " + str(value) + "\n")

    def personas_por_provincia(self):
        """Genera el archivo "personas_por_provincia.txt" """
        dicc = {}

        for p in self.__personas:
            provincia = p.get_provincia()
            lista_p = dicc.get(provincia, [])
            lista_p.append(p)
            dicc.update({provincia: lista_p})

        with open("personas_por_provincia.txt", "w", encoding="utf-8") as fw:
            for provincia, lista_p in dicc.items():
                fw.write(provincia + "\n")
                for _ in range(len(provincia)):
                    fw.write("-")
                fw.write("\n")

                for p in lista_p:
                    fw.write(str(p) + "\n")
                fw.write("\n")


# main

rp = RegistroDePersonas()

rp.get_personas("personas.csv")
p_mayores_de = rp.get_personas_mayores_que(28)
p_mayores_de.sort()
rp.escribir_personas(p_mayores_de, "personas-mayores-de-28.csv")
rp.cuantas_por_provincia()
rp.personas_por_provincia()
