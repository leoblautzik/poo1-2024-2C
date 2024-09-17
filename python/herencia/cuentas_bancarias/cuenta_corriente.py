"""Class Cuenta Corriente"""

from cuentas_bancarias.cuenta import Cuenta


class CuentaCorriente(Cuenta):
    """Class Cuenta Corriente
    Las cuentas corrientes pueden girar en descubierto hasta  un monto
    que se define al momento de su creación.
    """

    def __init__(self, dni, descubierto):
        super().__init__(dni)
        self.__descubierto = descubierto

    def get_descubierto(self):
        """Devuelve el descubierto definido en la cuenta"""
        return self.__descubierto

    def hay_dinero_suficiente(self, monto) -> bool:
        return super().get_saldo() + self.__descubierto >= monto

    def get_dinero_disponible(self) -> float:
        return super().get_saldo() + self.get_descubierto()

    def __str__(self) -> str:
        return super().__str__() + ", Descubierto: " + str(self.__descubierto)


if __name__ == "__main__":

    cc = CuentaCorriente(12345678, 10000)
    print(cc)
    cc.depositar(10000)
    print(cc)
    cc.extraer(15000)
    print(cc)
