import unittest
from src.logica.DesvEstandar import DesviacionEstandar
from src.logica.DesvEstandar import NoSePuedeCalcular


class PruebasDesvEstandar(unittest.TestCase):
    def setUp(self):
        self.DesviacionEstandar = DesviacionEstandar()

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            self.DesviacionEstandar.media()

if __name__ == '__main__':
    unittest.main()
