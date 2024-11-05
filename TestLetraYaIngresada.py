import unittest
from assignWord import Ahorcado 

class TestLetraYaIngresada(unittest.TestCase):
  def testLetraIncorrectaYaIngresada(self):
    palabra_secreta = 'hola'
    juego = Ahorcado(palabra_secreta)

    juego.adivinando(juego.palabra_secreta,'p')
    vidas_despues_primera_adiv = juego.vidas

    juego.adivinando(juego.palabra_secreta,'p')
    self.assertEqual(juego.vidas,vidas_despues_primera_adiv)
    
    
  def testLetraCorrectaYaIngresada(self):
    palabra_secreta = 'hola'
    juego = Ahorcado(palabra_secreta)

    juego.adivinando(juego.palabra_secreta,'a')
    vidas_despues_primera_adiv = juego.vidas

    juego.adivinando(juego.palabra_secreta,'a')
    self.assertEqual(juego.vidas,vidas_despues_primera_adiv)

if __name__=="__main__":
  unittest.main()      