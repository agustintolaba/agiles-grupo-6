import unittest
from assignWord import Ahorcado 

class TestContieneLetra(unittest.TestCase):
   

    def test_letra_minuscula_presente(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
        
        self.assertEqual(juego.verificaLetraEnLaPalabra(juego.palabra_secreta,'a'),True)

    def test_letra_minuscula_ausente(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'

        self.assertEqual(juego.verificaLetraEnLaPalabra(juego.palabra_secreta,'b'),False)

    def test_letra_mayuscula_presente(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'

        self.assertEqual(juego.verificaLetraEnLaPalabra(juego.palabra_secreta,'A'),True)

    def test_letra_mayuscula_ausente(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'

        self.assertEqual(juego.verificaLetraEnLaPalabra(juego.palabra_secreta,'B'),False)
        
if __name__=="__main__":
    unittest.main()       