"""Casos de prueba expresion balanceada"""

import unittest
from expresion_balanceada import ExpresionBalanceada


class TestExpresionBalanceada(unittest.TestCase):
    """Casos de prueba expresion balanceada"""

    def test_01(self):
        """Ejemplo del enunciado con una cadena balanceada"""
        eb = ExpresionBalanceada()
        expresion = "[()]{}{[()()]()}"
        self.assertTrue(eb.esta_balanceada(expresion))

    def test_02(self):
        """Ejemplo del enunciado con una cadena desbalanceada"""
        eb = ExpresionBalanceada()
        expresion = "[(])"
        self.assertFalse(eb.esta_balanceada(expresion))

    def test_03(self):
        """Ejemplo con una cadena vacia"""
        eb = ExpresionBalanceada()
        expresion = ""
        self.assertTrue(eb.esta_balanceada(expresion))

    def test_04(self):
        """Ejemplo una cadena de un solo simbolo de abrir"""
        eb = ExpresionBalanceada()
        expresion = "["
        self.assertFalse(eb.esta_balanceada(expresion))

    def test_05(self):
        """Ejemplo una cadena de un solo simbolo de cerrar"""
        eb = ExpresionBalanceada()
        expresion = "}"
        self.assertFalse(eb.esta_balanceada(expresion))

    def test_06(self):
        """Ejemplo una cadena con un simbolo incorrecto"""
        eb = ExpresionBalanceada()
        expresion = "{()[][]#}"
        with self.assertRaises(ValueError):
            eb.esta_balanceada(expresion)
