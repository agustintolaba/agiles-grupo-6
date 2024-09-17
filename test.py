import unittest
from assignWord import Ahorcado 

class TestAhorcado(unittest.TestCase):
  def setUp(self):
    self.palabras=['dualidad','sensibilidad','costos','reducidos','exponencial','hipergeometrica']

  def test_asignar_palabra_aleatoriamente(self):
    ahorcado=Ahorcado(self.palabras)
    palabra_asignada=ahorcado.asignar_palabra()
    #Prueba 

    self.assertIn(palabra_asignada,self.palabras)



if __name__=="__main__":
  unittest.main()       