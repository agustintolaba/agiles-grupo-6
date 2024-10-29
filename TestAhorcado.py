import unittest
from assignWord import Ahorcado 

class TestAhorcado(unittest.TestCase):

   

    def test_ganar_juego(self):
        ahorcado = Ahorcado('hola')
        palabra_manual = 'hola'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        ahorcado.adivinando(palabra_asignada,'H')
        ahorcado.adivinando(palabra_asignada,'O')
        ahorcado.adivinando(palabra_asignada,'L')
        ahorcado.adivinando(palabra_asignada,'A')
        self.assertTrue(ahorcado.ganado())