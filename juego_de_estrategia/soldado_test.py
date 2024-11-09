"""Pruebas unitarias del juego de estrategia"""

import unittest
from soldado import Soldado
from lancero import Lancero
from punial import Punial


class Pruebas(unittest.TestCase):

    # Soldado
    def test_puede_atacar(self):
        """Los soldados estan a 1 de distancia(cuerpo a cuerpo)
        y por lo tanto se pueden atacar"""
        s1 = Soldado(1)
        s2 = Soldado(2)
        self.assertTrue(s1.puede_atacar(s2))
        self.assertTrue(s2.puede_atacar(s1))

    def test_no_puede_atacar(self):
        """Los soldados estan fuera de alcance"""
        s1 = Soldado(1)
        s2 = Soldado(3)
        self.assertFalse(s1.puede_atacar(s2))
        self.assertFalse(s2.puede_atacar(s1))

    def test_no_se_puede_atacar_a_si_mismo(self):
        """Un soldano no se ataca a si mismo"""
        s1 = Soldado(1)
        s2 = Soldado(3)
        self.assertFalse(s1.puede_atacar(s1))
        self.assertFalse(s2.puede_atacar(s2))

    def test_no_puede_atacar_sin_energia(self):
        """Uno de los soldados ataca hasta quedarse sin energia"""
        s1 = Soldado(1)
        s2 = Soldado(2)
        for _ in range(10):
            s1.atacar(s2)
        self.assertFalse(s1.puede_atacar(s2))
        self.assertEqual(100, s2.get_salud())

    def test_no_puede_atacar_sin_energia_restaura_racion(self):
        """Uno de los soldados ataca hasta quedarse sin energia"""
        s1 = Soldado(1)
        s2 = Soldado(2)
        for _ in range(10):
            s1.atacar(s2)
        self.assertFalse(s1.puede_atacar(s2))
        self.assertEqual(0, s1.get_energia())
        s1.beber_agua()
        self.assertEqual(100, s1.get_energia())

    def test_soldados_iguales(self):
        """Dos objetos con los mismos valores para su estado, True
        por estar implementado el eq"""
        s1 = Soldado(1)
        s2 = Soldado(1)
        self.assertTrue(s1 == s2)

    def test_soldados_no_iguales(self):
        """Dos objetos con los algun valor distinto para sus estados, False
        por estar implementado el eq"""
        s1 = Soldado(1)
        s2 = Soldado(2)
        s1.atacar(s2)
        self.assertFalse(s1 == s2)

    def test_soldado_str(self):
        """Probamos el str"""
        s1 = Soldado(1)
        s2 = Soldado(10)
        print(s1)
        print(s2)

    def test_lancero_ataca_soldado(self):
        """Los soldados estan a 1 de distancia(cuerpo a cuerpo)
        y por lo tanto se pueden atacar"""
        l1 = Lancero(1)
        s2 = Soldado(2)
        self.assertTrue(l1.puede_atacar(s2))
        self.assertTrue(s2.puede_atacar(l1))

    def test_soldado_con_punial(self):
        """ "Soldado con punial"""
        s1 = Soldado(1)
        s2 = Soldado(2)
        s1 = Punial(s1)

        self.assertTrue(s1.puede_atacar(s2))
        self.assertTrue(s2.puede_atacar(s1))
        s1.atacar(s2)
        s2.atacar(s1)
        self.assertEqual(187, s2.get_salud())
        self.assertEqual(193, s1.get_salud())


if __name__ == "__main__":
    unittest.main()
