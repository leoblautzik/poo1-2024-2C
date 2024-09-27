import unittest
from caballero import Caballero
from soldado import Soldado


class Pruebas(unittest.TestCase):
    """Pruebas unitarias class Caballero"""

    # Arquero
    def test_puede_atacar(self):
        """Caballero ataca soldadito indefenso"""
        c1 = Caballero(1)
        s1 = Soldado(3)
        self.assertTrue(c1.puede_atacar(s1))

    def test_ataca_3_veces(self):
        """Caballero ataca soldadito indefenso"""
        c1 = Caballero(1)
        s1 = Soldado(3)
        self.assertTrue(c1.puede_atacar(s1))
        c1.atacar(s1)
        self.assertTrue(c1.puede_atacar(s1))
        c1.atacar(s1)
        self.assertTrue(c1.puede_atacar(s1))
        c1.atacar(s1)
        self.assertTrue(
            c1.get_caballo_rebelde()
        )  # estoy probando el caballo en la class caballero y eso esta mal
        self.assertFalse(c1.puede_atacar(s1))


if __name__ == "__main__":
    unittest.main()
