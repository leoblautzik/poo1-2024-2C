"""Pruebas unitarias para los metodos de la class Cubo"""

import unittest

from src import cubo


class CuboTest(unittest.TestCase):
    """Pruebas unitarias class Cubo"""

    def test_volumen(self):
        """Volumen del cubo"""
        cubito = cubo.Cubo(5)
        self.assertEqual(125, cubito.get_volumen())

    def test_area_cara(self):
        """Calcula el area de la cara de un cubo de lado 5"""
        cubito = cubo.Cubo(5)
        self.assertEqual(25, cubito.get_area_cara())

    def test_set_area(self):
        """Cambia el area de la cara a 64, el lado debe quedar en 8"""
        cubito = cubo.Cubo(5)
        self.assertEqual(5, cubito.get_lado())
        cubito.set_area(64)
        self.assertEqual(8, cubito.get_lado())

    def test_set_volumen(self):
        """Cambia el volumen del cubo a 64, el lado debe quedar en 4"""
        cubito = cubo.Cubo(5)
        self.assertEqual(5, cubito.get_lado())
        cubito.set_volumen(64)
        self.assertEqual(4, cubito.get_lado())


if __name__ == "__main__":
    unittest.main()
