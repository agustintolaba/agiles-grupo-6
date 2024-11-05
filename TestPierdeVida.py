import unittest
from assignWord import Ahorcado 

class TestPierdeVida(unittest.TestCase):

    def test_pierdeUnavida(self):
        palabra_secreta = 'operativa'
        juego = Ahorcado(palabra_secreta)
        vidas_iniciales = juego.vidas
        juego.adivinando(juego.palabra_secreta,'z')
        self.assertEqual(juego.vidas,(vidas_iniciales-1))

    
    def test_NopierdeUnavida(self):
        palabra_secreta = 'operativa'
        juego = Ahorcado(palabra_secreta)
        vidas_iniciales = juego.vidas
        juego.adivinando(juego.palabra_secreta,'a')
        self.assertEqual(juego.vidas,vidas_iniciales)

if __name__=="__main__":
  unittest.main()      