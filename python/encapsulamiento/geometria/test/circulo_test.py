"""Pruebas unitarias para Circulo"""

import unittest
from src import circulo


class CirculoTest(unittest.TestCase):
    """Pruebas unitarias class Circulo"""

    def test_get_radio(self):
        """get_radio() test"""
        c1 = circulo.Circulo(5, 1, 1)
        esperado = 5.0
        obtenido = c1.get_radio()
        self.assertEqual(esperado, obtenido)

    def test_constructor_por_defecto(self):
        """Constructor por defecto"""
        c = circulo.Circulo()
        self.assertEqual(1, c.get_radio())

    def test_exception_con_radio_negativo(self):
        """Se comprueba que se lanza la exception
        si el radio es negativo"""
        with self.assertRaises(ValueError):
            circulo.Circulo(-1, 1, 1)

    def test_exception_set_radio_con_radio_negativo(self):
        """Se comprueba que se lanza la exception
        si el radio es negativo"""
        c1 = circulo.Circulo(1, 1, 1)
        with self.assertRaises(ValueError):
            c1.set_radio(-1)


if __name__ == "__main__":
    unittest.main()
