"""Pruebas unitarias para Circulo"""

import unittest
import circulo


class Pruebas(unittest.TestCase):
    """Pruebas unitarias class Circulo"""

    def test_get_radio(self):
        """get_radio() test"""
        c1 = circulo.Circulo(5, 1, 1)
        esperado = 5.0
        obtenido = c1.get_radio()
        self.assertEqual(esperado, obtenido)

    def test_exception_con_radio_negativo(self):
        """Se comprueba que se lanza la exception
        si el radio es negativo"""
        with self.assertRaises(ValueError):
            circulo.Circulo(-1, 1, 1)


unittest.main()
