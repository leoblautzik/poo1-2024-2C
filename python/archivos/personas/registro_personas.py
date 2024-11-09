"""class RegistroPersonas"""

from persona import Persona


class RegistroDePersonas:
    """class RegistroDePersonas"""

    def get_personas(self, archivo):
        """Implementar un método get_personas  de la class RegistroPersonas que
        reciba el nombre de un archivo y devuelva una lista de Personas con personas
        que fueron leídas del archivo de texto personas.csv
        con formato "dni,apellido,edad,provincia"."""

        personas = []
        with open(archivo, "r", encoding="utf-8") as file:
            for cada_linea in file:
                # para cada linea creo un objeto persona y lo agrego a la lista personas
                datos = cada_linea.split(",")
                persona = Persona(int(datos[0]), datos[1], int(datos[2]), datos[3])
                personas.append(persona)

        return personas

    def escribir_personas_mayores_de(self, lista, edad):
        """Implementar un método getPersonasMayoresAEdad que reciba una lista de Personas
        y una edad y devuelva otra lista de Personas con las personas cuyas edades
        son mayores a esa edad.
        Guardar esas personas en un archivo “personasMayoresDeXX.out”,
        donde xx sea la edad que se usó como parámetro.
        Guardarlo ordenado alfabéticamente por apellido."""

        personas_mayores = self.get_personas_mayores_de(lista, edad)

        with open(
            "personas_mayores_de_" + str(edad) + ".csv", "w", encoding="utf-8"
        ) as fpm:
            for cada_persona in personas_mayores:
                fpm.write(str(cada_persona))

    def get_personas_mayores_de(self, lista, edad):
        """Implementar un método getPersonasMayoresAEdad que reciba una lista de Personas
        y una edad y devuelva otra lista de Personas con las personas cuyas edades
        son mayores a esa edad."""
        personas_mayores = []
        for p in lista:
            if p.get_edad() > edad:
                personas_mayores.append(p)

        return personas_mayores

    def edad_promedio(self, lista) -> int:
        """Implementar un método que devuelva la edad promedio de la muestra de personas."""
        suma = 0
        for p in lista:
            suma += p.get_edad()

        if len(lista) == 0:
            return 0
        return suma // len(lista)

    def get_personas_por_provincia(self, personas):
        """devuelve un diccionario cuyas keys son las provincias
        y para cada una, el value asocoado es una lista con las personas
        de esa provincia"""
        dicc = {}
        for cp in personas:
            key = cp.get_provincia()
            value = dicc.get(key, [])
            value.append(cp)
            dicc.update({key: value})

        return dicc

    def escribir_por_provincia(self, dicc):
        with open("provincias.txt", "w", encoding="utf-8") as file:
            for provi in dicc:
                file.write("\n" + provi)
                for p in dicc[provi]:
                    file.write(str(p))


# main
rp = RegistroDePersonas()
lista_de_personas = rp.get_personas("personas.csv")
# rp.get_personas_mayores_de(lista_de_personas, 37)
# rp.get_personas_mayores_de(lista_de_personas, 25)
# print("Edad promedio:", rp.edad_promedio(lista_de_personas))
#
# lm = rp.get_personas_mayores_de(lista_de_personas, 40)
# print("Edad promedio de los mayores de 40", rp.edad_promedio(lm))

rp.escribir_por_provincia(rp.get_personas_por_provincia(lista_de_personas))
