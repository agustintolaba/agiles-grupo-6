import unittest
from assignWord import Ahorcado 

class TestLongitudPalabra(unittest.TestCase):
  def Test_informaCantidadDeLetrasPalabraCorta(self):
    palabra_manual = 'Hola'
    palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
    self.assertEqual(ahorcado.informaCantidadDeLetrasDeLaPalabra(palabra_asignada),4)

if __name__=="__main__":
    ahorcado = Ahorcado()
    print("Ejecutando tests...")
    unittest.main()    