"""Class CajaDeAhorro"""


class CajaDeAhorro:
    """Modelamos una Caja de Ahorros
    Se podrá consultar el saldo, obtener el titular y
    las operaciones: depositar extraer y transferir
    """

    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0

    def obtener_titular(self):
        """Retorna el titular de la cuenta"""
        return self.__titular

    def consultar_saldo(self):
        """Retorna el saldo actual de la cuenta"""
        return self.__saldo

    def depositar(self, monto):
        """pre: monto no puede ser cero o negativo
        pos: Incrementa el saldo en monto
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto

    def extraer(self, monto):
        """pre: monto debe ser mayor a cero
        y debe haber saldo suficiente para realizar la operacion.
        pos: Decrementa el saldo en monto
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if self.__hay_saldo_suficiente(monto):
            self.__saldo -= monto

    def transferir(self, destino, monto):
        """pre: monto debe ser mayor a cero
        y debe haber saldo suficiente en la cuenta origen(self) para realizar la operacion.
        pos: Incrementa el saldo de la cuenta destino.
        Decrementa el saldo de la cuenta origen.
        """
        if self.__hay_saldo_suficiente(monto):
            self.extraer(monto)
            destino.depositar(monto)

    def __hay_saldo_suficiente(self, monto) -> bool:
        """retorna el true si hay saldo es mayor al monto por el que se consulta"""
        return self.__saldo >= monto
