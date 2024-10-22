import unittest
from src.logica.DesvEstandar import DesviacionEstandar
from src.logica.DesvEstandar import NoSePuedeCalcular


class PruebasDesvEstandar(unittest.TestCase):
    def setUp(self):
        self.DesviacionEstandar = DesviacionEstandar()

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            self.DesviacionEstandar.media()

    def test_media_un_elemento(self):
        self.DesviacionEstandar.agregar_elemento(5)
        self.assertEqual(self.DesviacionEstandar.media(), 5)


if __name__ == '__main__':
    unittest.main()
