import unittest
from assignWord import Ahorcado 

class TestArriesgaPalabra(unittest.TestCase):
   

    def test_palabraVacia(self):

        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
                
        self.assertEqual(juego.arriesgaPalabra(juego.palabra_secreta,''),False)

    def test_palabraCorrectaMinuscula(self):
       
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
                
        self.assertEqual(juego.arriesgaPalabra(juego.palabra_secreta,'operativa'),True)

    def test_palabraIncorrectaMinuscula(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
                
        self.assertEqual(juego.verificaLetraEnLaPalabra(juego.palabra_secreta,'hola'),False)

    def test_palabraCorrectaMayuscula(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
        
        self.assertEqual(juego.arriesgaPalabra(juego.palabra_secreta,'OPERATIVA'),True)

    def test_palabraIncorrectaMayuscula(self):
        
        juego = Ahorcado()
        juego.palabra_secreta = 'operativa'
        
        self.assertEqual(juego.arriesgaPalabra(juego.palabra_secreta,'APROBADO'),False)
   
        
if __name__=="__main__":
    unittest.main()       