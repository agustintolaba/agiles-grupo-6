import unittest
from assignWord import Ahorcado 

class TestLetraYaIngresada(unittest.TestCase):

  def testLetraIncorrectaYaIngresada(self):
  
    juego = Ahorcado()
    juego.palabra_secreta = 'operativa'
    juego.intento('w')
    self.assertEqual(juego.vidas_restantes , 4)
    self.assertTrue(juego.letras_arriesgadas_en_el_juego,'w')
    juego.intento('w')
    self.assertEqual(juego.vidas_restantes , 4)
    self.assertTrue(juego.letras_arriesgadas_en_el_juego,'w')
    
  def testLetraCorrectaYaIngresada(self):

    juego = Ahorcado()
    juego.palabra_secreta = 'operativa'
    juego.intento('p')
    self.assertEqual(juego.vidas_restantes , 5)
    self.assertTrue(juego.letras_arriesgadas_en_el_juego,'p')
    juego.intento('p')
    self.assertEqual(juego.vidas_restantes , 5)
    self.assertTrue(juego.letras_arriesgadas_en_el_juego,'p')

if __name__=="__main__":
  unittest.main()      