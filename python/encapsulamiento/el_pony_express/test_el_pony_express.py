"""Test El Pony Express"""

import unittest
import el_pony_express


class TestPony(unittest.TestCase):
    """Casos de prueba para el Pony Express"""

    def test_1(self):
        """Dos estaciones, alcanza con un solo caballo"""
        d = [18, 15]
        self.assertEqual(1, el_pony_express.caballos(d))

    def test_2(self):
        """Debe cambiar de caballo antes de la tercer estacion"""
        d = [43, 23, 40, 13]
        self.assertEqual(2, el_pony_express.caballos(d))

    def test_3(self):
        """Dos cambios de caballo, debe devolver 3"""
        d = [33, 8, 16, 47, 30, 30, 46]
        self.assertEqual(3, el_pony_express.caballos(d))

    def test_4(self):
        """Cada estacion debe cambiar de caballo"""
        d = [51, 51, 51]
        self.assertEqual(3, el_pony_express.caballos(d))

    def test_5(self):
        """Cada estacion debe cambiar de caballo"""
        d = [6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]
        self.assertEqual(4, el_pony_express.caballos(d))

    def test_10(self):
        """Dos estaciones, la segunda inalcanzable"""
        d = [18, 101]
        with self.assertRaises(ValueError):
            el_pony_express.caballos(d)


if __name__ == "__main__":
    unittest.main()
