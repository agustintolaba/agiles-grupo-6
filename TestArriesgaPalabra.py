import unittest
from assignWord import Ahorcado 

class TestArriesgaPalabra(unittest.TestCase):
   

    def test_palabraVacia(self):
        ahorcado = Ahorcado('operativa')
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.arriesgaPalabra(palabra_asignada,''),False)

    def test_palabraCorrectaMinuscula(self):
        ahorcado = Ahorcado('operativa')
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'operativa'),True)

    def test_palabraIncorrectaMinuscula(self):
        ahorcado = Ahorcado('operativa')
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'hola'),False)

    def test_palabraCorrectaMayuscula(self):
        ahorcado = Ahorcado('operativa')
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'OPERATIVA'),True)

    def test_palabraIncorrectaMayuscula(self):
        ahorcado = Ahorcado('operativa')
        palabra_manual = 'operativa'
        palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)
        self.assertEqual(ahorcado.verificaLetraEnLaPalabra(palabra_asignada,'HOLA'),False)
   
        
if __name__=="__main__":
    unittest.main()       