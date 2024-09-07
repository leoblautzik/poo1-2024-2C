"""Test unitarios Caja Ahorro"""

import unittest
from cuentas_bancarias import caja_ahorro


class CajaAhorroTest(unittest.TestCase):
    """Test unitarios CA"""

    def test_obtener_saldo(self):
        """El saldo de la cuenta debe estar en cero luego de ser
        instanciada"""
        c = caja_ahorro.CajaDeAhorro("Pirulo")
        self.assertEqual(0, c.consultar_saldo())

    def test_obtener_titular(self):
        """obtener titular test"""
        c = caja_ahorro.CajaDeAhorro("Pirulo")
        self.assertEqual("Pirulo", c.obtener_titular())

    def test_depositar_1000(self):
        """El saldo de la cuenta se incrementa en 1000
        luego de depositar ese importe"""
        c = caja_ahorro.CajaDeAhorro("Juam Perez")
        c.depositar(1000)
        self.assertEqual(1000, c.consultar_saldo())

    def test_depositar_monto_negativo(self):
        """El metodo depositar lanza un error al intentar
        depositar un monto cero o negativo"""
        c = caja_ahorro.CajaDeAhorro("Julian")
        with self.assertRaises(ValueError):
            c.depositar(-1)

    def test_extraer_con_saldo_suficiente(self):
        """El saldo de la cuenta se reduce luego de la extraccion"""
        c = caja_ahorro.CajaDeAhorro("Juam Perez")
        c.depositar(1000)
        self.assertEqual(1000, c.consultar_saldo())
        c.extraer(500)
        self.assertEqual(500, c.consultar_saldo())


if __name__ == "__main__":
    unittest.main()
