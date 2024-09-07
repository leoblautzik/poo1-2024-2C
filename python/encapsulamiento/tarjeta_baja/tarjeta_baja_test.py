"""Pruebas unitarias TarjetaBaja"""
import unittest
# from paquete import modulo
from tarjeta_baja import tarjeta_baja


class TarjetaBajaTest(unittest.TestCase):

    def test_saldo_inicial(self):
        """Saldo inicial de 100 pe"""
        t = tarjeta_baja.TarjetaBaja(100)
        self.assertEqual(100.1, t.obtener_saldo())

    def test_saldo_luego_de_un_bondi(self):
        t = tarjeta_baja.TarjetaBaja(100)
        t.pagar_viaje_en_colectivo()
        self.assertEqual(78.50, t.obtener_saldo())

    def test_saldo_luego_de_un_subte(self):
        t = tarjeta_baja.TarjetaBaja(100)
        t.pagar_viaje_en_subte()
        self.assertEqual(80.5, t.obtener_saldo())


if __name__ == "__main__":
    unittest.main()
