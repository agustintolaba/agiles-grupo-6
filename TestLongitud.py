import unittest
from assignWord import Ahorcado 

class TestLongitudPalabra(unittest.TestCase):
  
  def test_informaCantidadDeLetrasPalabraVacia(self):
    
    palabra_secreta = ''
    juego = Ahorcado(palabra_secreta)
    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),0)

  def test_informaCantidadDeLetrasPalabraLarga(self):
    palabra_secreta = 'operativa'
    juego = Ahorcado(palabra_secreta)
    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),9)

  def test_informaCantidadDeLetrasPalabraCorta(self):
    palabra_secreta = 'hola'
    juego = Ahorcado(palabra_secreta)
    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),4)

if __name__=="__main__":
  unittest.main()       