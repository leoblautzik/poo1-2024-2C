"""Class Persona"""


class Persona:
    """class Persona"""

    def __init__(self, dni, apellido, edad, provincia):
        self.__dni = dni
        self.__apellido = apellido
        self.__edad = edad
        self.__provincia = provincia

    def __str__(self) -> str:
        return (
            str(self.__dni)
            + ","
            + self.__apellido
            + ","
            + str(self.__edad)
            + ","
            + self.__provincia
        )

    def get_apellido(self):
        return self.__apellido

    def __lt__(self, other):
        return self.__apellido < other.get_apellido()

    def __gt__(self, other):
        return self.__apellido > other.get_apellido()

    def get_edad(self) -> int:
        """Devuelve un entero que es la edad de la persona"""
        return self.__edad

    def get_provincia(self) -> str:
        """devuelve un string que es la provincia de origen de la persona"""
        return self.__provincia
