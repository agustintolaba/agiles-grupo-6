import unittest
from assignWord import Ahorcado 

class TestAhorcado(unittest.TestCase):

   

    def test_ganar_juego(self):
        ahorcado = Ahorcado('hola')
        palabra_manual = 'hola'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        ahorcado.adivinando(palabra_asignada,'h')
        ahorcado.adivinando(palabra_asignada,'o')
        ahorcado.adivinando(palabra_asignada,'l')
        ahorcado.adivinando(palabra_asignada,'a')
        self.assertTrue(ahorcado.ganado())
