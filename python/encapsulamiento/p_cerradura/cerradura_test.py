"""Pruebas unitarias class Cerradura"""

import unittest
from p_cerradura import cerradura


class CerraduraTest(unittest.TestCase):
    """Casos de prueba para la cerradura de combinacion"""

    def test_cerradura_nueva(self):
        """Cerradura nueva inicia en estado abierta y no bloqueada"""
        ce1 = cerradura.Cerradura(123, 3)
        self.assertTrue(ce1.esta_abierta())
        self.assertFalse(ce1.esta_cerrada())
        self.assertFalse(ce1.fue_bloqueada())

    def test_cerradura_cerrar(self):
        """Cerradura nueva y se cierra"""
        ce1 = cerradura.Cerradura(123, 3)
        ce1.cerrar()
        self.assertFalse(ce1.esta_abierta())
        self.assertTrue(ce1.esta_cerrada())

    def test_cerradura_falla_hasta_bloquear(self):
        """Cerradura nueva y se cierra, lue=go se falla hasta bloquear"""
        ce1 = cerradura.Cerradura(123, 3)
        ce1.cerrar()
        ce1.abrir(124)
        ce1.abrir(111)
        ce1.abrir(222)
        self.assertTrue(ce1.fue_bloqueada())
        self.assertEqual(3, ce1.contar_aperturas_fallidas())

    def test_cerradura_falla_abre(self):
        """Cerradura nueva y se cierra, luego se falla dos veces
        y abre al tercer intento"""
        ce1 = cerradura.Cerradura(123, 3)
        ce1.cerrar()
        ce1.abrir(124)
        ce1.abrir(111)
        ce1.abrir(123)
        self.assertTrue(ce1.esta_abierta())
        self.assertFalse(ce1.fue_bloqueada())
        self.assertEqual(2, ce1.contar_aperturas_fallidas())

    def test_contar_fallos(self):
        """Cerradura nueva y se cierra, luego se falla dos veces
        y abre al tercer intento.
        Se repite dos veces"""
        ce1 = cerradura.Cerradura(123, 3)
        ce1.cerrar()
        ce1.abrir(124)
        ce1.abrir(111)
        ce1.abrir(123)
        ce1.cerrar()
        ce1.abrir(124)
        ce1.abrir(111)
        ce1.abrir(123)
        self.assertEqual(4, ce1.contar_aperturas_fallidas())
        self.assertEqual(2, ce1.contar_aperturas_exitosas())


if __name__ == "__main__":
    unittest.main()
