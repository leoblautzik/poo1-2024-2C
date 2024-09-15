"""Class Caja de Ahorro"""

from cuentas_bancarias import cuenta as c


class CajaDeAhorro(c.Cuenta):
    """Class Caja de Ahorro: Las cuentas de ahorro no pueden tener números rojos.
    Ademas del saldo, tienen una reserva donde el titular reserva dinero.
    Ese pozo de reserva no se informa como parte del saldo disponible,
    pero de allí se puede recuperar dinero y pasarlo al saldo.
    """

    def __init__(self, dni):
        super().__init__(dni)
        self.__reserva = 0.00

    def extraer(self, monto):
        if not self.hay_dinero_suficiente(monto):
            raise ValueError("Saldo insuficiente")
        super().set_saldo(super().get_saldo - monto)

    def hay_dinero_suficiente(self, monto) -> bool:
        """Devuelve true o false, segun alcance el saldo para
        hacer la operacion"""
        return super().get_saldo() >= monto

    def reservar(self, monto):
        """Reserva en la reservarva una parte del saldo"""
        if monto <= self.get_saldo():
            self.__reserva += monto
            super().set_saldo(self.get_saldo() - monto)

    def recuperar(self, monto):
        """Incorpora al saldo el monto indicado, desde la reserva"""
        if monto <= self.__reserva:
            self.__reserva -= monto
            super().set_saldo(self.get_saldo() + monto)

    def get_reserva(self):
        """Devuelve cuanto dinero hay disponible en la reserva"""
        return self.__reserva

    def get_dinero_disponible(self) -> float:
        return super().get_saldo() + self.get_reserva()

    def __str__(self) -> str:
        return super().__str__() + ", Reserva: " + str(self.__reserva)


if __name__ == "__main__":
    ca = CajaDeAhorro(12345678)
    print(ca)
    ca.depositar(1000)
    ca.reservar(500)
    print(ca.get_reserva())
    print(ca)
    print(ca.get_dinero_disponible())
