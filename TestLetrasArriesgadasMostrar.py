import unittest
from assignWord import Ahorcado 

class TestLetrasArriesgadasMostrar(unittest.TestCase):

   

    def test_mostrar_letra_correcta_una_letra_acertada(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'gato'
    
        juego.letras_arriesgada = ["a"]
        juego.mostrar_letra_correcta("a")
        self.assertEqual( juego.palabra_a_mostrar , ["_", "a", "_", "_"])

        
    def test_mostrar_letra_correcta_varias_letras_acertadas(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'gato'

        juego.letras_arriesgada = ["a", "t"]
        juego.mostrar_letra_correcta("a")
        juego.mostrar_letra_correcta("t")
        
        self.assertEqual(juego.palabra_a_mostrar , ["_", "a", "t", "_"])
  
    def test_mostrar_letra_correcta_con_letra_repetida(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'papa'

        juego.letras_arriesgada = ["p"]
        juego.mostrar_letra_correcta("p")

        self.assertEqual(juego.palabra_a_mostrar , ["p", "_", "p", "_"])

    def test_mostrar_letra_correcta_letra_no_acertada(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'gato'

        juego.letras_arriesgada = ["z"]
        juego.mostrar_letra_correcta("z")
        self.assertEqual(juego.palabra_a_mostrar , ["_", "_", "_", "_"])

    def test_mostrar_letra_correcta_todas_letras_acertadas(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'gato'

        juego.letras_arriesgada = ["g", "a", "t", "o"]
        juego.mostrar_letra_correcta("g")
        juego.mostrar_letra_correcta("a")
        juego.mostrar_letra_correcta("t")
        juego.mostrar_letra_correcta("o")

        assert juego.palabra_a_mostrar == ["g", "a", "t", "o"]
        

if __name__=="__main__":
  unittest.main()      