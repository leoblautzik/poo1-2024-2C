"""Casos de prueba para Arquero"""

import unittest
from arquero import Arquero
from soldado import Soldado


class Pruebas(unittest.TestCase):
    """Pruebas unitarias class Arquero"""

    # Arquero
    def test_puede_atacar(self):
        """Arquero ataca soldadito indefenso"""
        a1 = Arquero(1)
        s1 = Soldado(3)

        self.assertTrue(a1.puede_atacar(s1))

    def test_puede_atacar_limite_distancia(self):
        """Arquero no ataca soldadito a la distania maxima"""
        a1 = Arquero(1)
        s1 = Soldado(6)

        self.assertTrue(a1.puede_atacar(s1))

    def test_no_puede_atacar(self):
        """Arquero no ataca soldadito lejano"""
        a1 = Arquero(1)
        s1 = Soldado(7)

        self.assertFalse(a1.puede_atacar(s1))

    def test_atacar_soldado(self):
        """Arquero ataca soldadito indefenso"""
        a1 = Arquero(1)
        s1 = Soldado(3)
        a1.atacar(s1)
        self.assertEqual(19, a1.get_flechas())
        self.assertEqual(195, s1.get_salud())

    def test_atacar_hasta_quedar_sin_flechas(self):
        """Arquero ataca soldadito 20 veces"""
        a1 = Arquero(1)
        s1 = Soldado(3)
        for _ in range(20):
            a1.atacar(s1)
        self.assertEqual(0, a1.get_flechas())
        self.assertEqual(100, s1.get_salud())
        self.assertFalse(a1.puede_atacar(s1))

    def test_atacar_hasta_quedar_sin_flechas_recrga(self):
        """Arquero ataca soldadito 20 veces y despues 5 mas"""
        a1 = Arquero(1)
        s1 = Soldado(3)
        for _ in range(20):
            a1.atacar(s1)
        self.assertEqual(0, a1.get_flechas())
        self.assertEqual(100, s1.get_salud())
        self.assertFalse(a1.puede_atacar(s1))
        a1.recargar_flechas()
        for _ in range(5):
            a1.atacar(s1)
        self.assertEqual(1, a1.get_flechas())
        self.assertEqual(75, s1.get_salud())

    def test_atacar_hasta_quedar_sin_flechas_venganza(self):
        """Arquero ataca soldadito 20 veces y el soldado lo liquida"""
        a1 = Arquero(1)
        s1 = Soldado(3)
        for _ in range(20):
            a1.atacar(s1)
        self.assertEqual(0, a1.get_flechas())
        self.assertEqual(100, s1.get_salud())
        self.assertFalse(a1.puede_atacar(s1))
        # Ahora el soldado lo ataca hasta matarlo
        s1.desplazarse(2)
        for _ in range(5):
            s1.atacar(a1)
        self.assertTrue(a1.esta_muerto())


if __name__ == "__main__":
    unittest.main()
