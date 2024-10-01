import unittest
from assignWord import Ahorcado 

class TestAhorcado(unittest.TestCase):
#  def setUp(self):
#   self.palabras=['dualidad','sensibilidad','costos','reducidos','exponencial','hipergeometrica']

  def test_asignar_palabra_manualmente(self):
    ahorcado=Ahorcado()
    palabra_manual = 'operativa'
    palabra_asignada= ahorcado.ingresa_palabra(palabra_manual)

    self.assertEqual(palabra_asignada,palabra_manual)
    self.assertNotEqual('',palabra_manual)


if __name__=="__main__":
  unittest.main()       


