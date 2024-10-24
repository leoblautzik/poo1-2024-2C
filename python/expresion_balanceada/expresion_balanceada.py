"""
Consigna: Escribir un método que evalúa si una cadena de paréntesis, 
corchetes y llaves está bien balanceada y devuelve true si 
está bien balanceada y false si está mal balanceada. 
Por ejemplo: [()]{}{[()()]()} debe devolver true, 
mientras que [(]) debe devolver false. 
"""


class ExpresionBalanceada:
    """Para resolver la consigna se utiliza una pila para apilar los simbolos de abrir.
    Si el simbolo que se lee es de cerrar, se desapila y se compueba que  concuerde con el leido,
    si no hay concordancia con el par de cierre, se devuelve False.
    Si hay concordancia, se continua evaluando hasta el fin de la expresion.
    Si al finalizar la iteración sobre la expresion, la pila queda vacia,
    entonces la expresion está balanceada"""

    def __init__(self):
        ## Estructuras auxiliares

        # un set para saber si es de abrir
        self.__de_abrir = {"[", "(", "{"}

        # un set para saber si es de cerrar
        self.__de_cerrar = {"]", ")", "}"}

        # un diccionario para encontrar el parcito
        self.__parejita = {"]": "[", ")": "(", "}": "{"}

        # una pila para apilar los simbolos de abrir
        self.__pila = []

    def __pila_vacia(self) -> bool:
        return len(self.__pila) == 0

    def esta_balanceada(self, exp) -> bool:
        """Evalúá si la expresion esta bien balanceada
        Lanza un error si la expresion contiene simbolos diferentes a ()[]{}
        """

        for simbolo in exp:

            if simbolo in self.__de_abrir:
                self.__pila.append(simbolo)
            elif simbolo in self.__de_cerrar:
                if self.__pila_vacia() or self.__parejita[simbolo] != self.__pila.pop():
                    return False
            else:
                raise ValueError("Simbolo incorrecto")

        return self.__pila_vacia()
