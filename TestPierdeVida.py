import unittest
from assignWord import * 

class TestPierdeVida(unittest.TestCase):

    def test_pierdeUnavida(self):
        juego = Ahorcado()

        juego.palabra_secreta = 'operativa'
        letra = 'w'
        self.assertEqual(juego.intento(letra), False )
        self.assertEqual(len(juego.letras_adivinadas) , 0)
        self.assertEqual(letra in juego.letras_adivinadas , False)
        self.assertEqual(juego.vidas_restantes , 4)
        

    
    def test_NopierdeUnavida(self):
        juego = Ahorcado()

        juego.palabra_secreta = 'operativa'
        letra = 'a'
        self.assertEqual(juego.intento(letra) ,True )
        self.assertEqual(letra in juego.letras_adivinadas, True)
        self.assertEqual(len(juego.letras_adivinadas) , 1)
        self.assertEqual(juego.vidas_restantes, 5)

if __name__=="__main__":
  unittest.main()      