import unittest
from assignWord import Ahorcado 

class TestAhorcado(unittest.TestCase):

   

    def test_ganar_juego(self):
        palabra_secreta = 'hola'
        juego = Ahorcado(palabra_secreta)
        juego.adivinando(juego.palabra_secreta,'h')
        juego.adivinando(juego.palabra_secreta,'o')
        juego.adivinando(juego.palabra_secreta,'l')
        juego.adivinando(juego.palabra_secreta,'a')
        self.assertTrue(juego.ganado())

        
        
    def test_perder_juego(self):
        palabra_secreta = 'hola'
        juego = Ahorcado(palabra_secreta)
        juego.adivinando(juego.palabra_secreta,'x')
        juego.adivinando(juego.palabra_secreta,'j')
        juego.adivinando(juego.palabra_secreta,'f')
        self.assertTrue(juego.perdido())
        

if __name__=="__main__":
  unittest.main()      