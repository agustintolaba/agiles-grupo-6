import unittest
from assignWord import Ahorcado 

class TestLongitudPalabra(unittest.TestCase):
  
  def test_informaCantidadDeLetrasPalabraVacia(self):
    
    juego = Ahorcado()
    juego.palabra_secreta = ''

    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),0)

  def test_informaCantidadDeLetrasPalabraLarga(self):
    
    juego = Ahorcado()
    juego.palabra_secreta = 'operativa'
    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),9)

  def test_informaCantidadDeLetrasPalabraCorta(self):
    
    juego = Ahorcado()
    juego.palabra_secreta = 'hola'
    self.assertEqual(juego.informaCantidadDeLetrasDeLaPalabra(juego.palabra_secreta),4)

if __name__=="__main__":
  unittest.main()       