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

    def test_media_dos_elementos(self):
        self.DesviacionEstandar.agregar_elemento(4)
        self.DesviacionEstandar.agregar_elemento(6)
        self.assertEqual(self.DesviacionEstandar.media(), 5)

    def test_media_n_elementos_positivos(self):
        for i in range(1, 6):
            self.DesviacionEstandar.agregar_elemento(i)
        self.assertEqual(self.DesviacionEstandar.media(), 3)

    def test_media_n_elementos_ceros(self):
        for _ in range(5):
            self.DesviacionEstandar.agregar_elemento(0)
        self.assertEqual(self.DesviacionEstandar.media(), 0)

    def test_media_n_elementos_positivos_y_negativos(self):
        self.DesviacionEstandar.agregar_elemento(-1)
        self.DesviacionEstandar.agregar_elemento(1)
        self.assertEqual(self.DesviacionEstandar.media(), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            self.DesviacionEstandar.agregar_elemento("a")
    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            self.DesviacionEstandar.desviacion_estandar()



if __name__ == '__main__':
    unittest.main()
