import unittest
from assignWord import Ahorcado 

class TestLetrasUsadas(unittest.TestCase):

    def test_letra_no_usada(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'gato'
        juego.intento('a')
        juego.intento('e')

        self.assertEqual( 'o' in juego.letras_arriesgada , False)
        self.assertEqual( 'u' in juego.letras_arriesgada , False)

    def test_letras_usadas(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'gato'
        juego.intento('a')
        juego.intento('e')

        self.assertEqual( 'a' in juego.letras_arriesgada , True)
        self.assertEqual( 'e' in juego.letras_arriesgada , True)

    def test_letras_usadas_vacia(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'gato'
        
        self.assertEqual( 'o' in juego.letras_arriesgada , False)
        self.assertEqual( 'u' in juego.letras_arriesgada , False)

if __name__=="__main__":
  unittest.main()      