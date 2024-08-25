"""Pruebas unitarias para los metodos de la class Punto"""

import unittest
import punto


class Pruebas(unittest.TestCase):
    """Pruebas unitarias class Punto"""

    def test_get_x(self):
        """get_x() test"""
        p1 = punto.Punto(3.0, 4.0)
        esperado = 3.0
        obtenido = p1.get_x()
        self.assertEqual(esperado, obtenido)

    def test_distancia_al_origen(self):
        """Distancia al origen test"""
        p1 = punto.Punto(3.0, 4.0)
        esperado = 5.0
        obtenido = p1.distancia_al_origen()
        self.assertEqual(esperado, obtenido)


unittest.main()
