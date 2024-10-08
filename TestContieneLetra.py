import unittest
from assignWord import Ahorcado 

class TestLongitudPalabra(unittest.TestCase):
   

    def test_letra_minuscula_presente(self):
        ahorcado = Ahorcado()
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'a'),True)

    def test_letra_minuscula_ausente(self):
        ahorcado = Ahorcado()
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'b'),False)

    def test_letra_mayuscula_presente(self):
        ahorcado = Ahorcado()
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'A'),True)

    def test_letra_mayuscula_ausente(self):
        ahorcado = Ahorcado()
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'B'),False)
if __name__=="__main__":
    unittest.main()       