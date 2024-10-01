import unittest
from assignWord import Ahorcado 

class TestLongitudPalabra(unittest.TestCase):
   

    def Test_informaCantidadDeLetrasPalabraVacia(self):
        ahorcado = Ahorcado()
        palabra_manual = ''
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.informaCantidadDeLetrasDeLaPalabra(palabra_asignada),0)

    def Test_informaCantidadDeLetrasPalabraLarga(self):
        ahorcado = Ahorcado()
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.informaCantidadDeLetrasDeLaPalabra(palabra_asignada),9)

    def Test_informaCantidadDeLetrasPalabraCorta(self):
        ahorcado = Ahorcado()
        palabra_manual = 'Hola'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.informaCantidadDeLetrasDeLaPalabra(palabra_asignada),4)


if __name__=="__main__":
  unittest.main()       