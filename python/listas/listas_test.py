import unittest
import listas


class ListasTest(unittest.TestCase):

    def test_eliminar_duplicados(self):
        """Por ejemplo, si la lista de entrada es: [1, 2, 2, 1, 4, 2, 4, 3],
        la salida sería: [1, 2, 4, 3].
        """
        lista = [1, 2, 2, 1, 4, 2, 4, 3]
        self.assertEqual([1, 2, 4, 3], listas.eliminar_duplicados(lista))
