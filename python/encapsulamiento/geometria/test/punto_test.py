"""Pruebas unitarias para los metodos de la class Punto"""

import unittest

from src import punto


class PuntoTest(unittest.TestCase):
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

    def test_esta_sobre_x(self):
        """Está sobre el eje x"""
        p1 = punto.Punto(3.0, 4.0)
        p2 = punto.Punto(3.0, 0.0)
        self.assertTrue(p2.esta_sobre_eje_x())
        self.assertFalse(p1.esta_sobre_eje_x())


if __name__ == "__main__":
    unittest.main()
