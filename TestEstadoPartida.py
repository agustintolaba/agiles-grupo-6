import unittest
from assignWord import Ahorcado 

class TestEstadoPartida(unittest.TestCase):


    def test_estado_del_juego(self):
      juego = Ahorcado()
      juego.palabra_secreta = "perro"
      juego.intento("p")
      juego.intento("e")
      self.assertEqual(juego.se_termino_el_juego(), False)

    def test_juego_terminado_con_ganador(self):

      juego = Ahorcado()
      juego.palabra_secreta = "perro"
      juego.intento("p")
      juego.intento("e")
      juego.intento("r")
      juego.intento("r")
      juego.intento("o")
      self.assertEqual(juego.se_termino_el_juego(), True)

    def test_juego_terminado_con_perdedor(self):

      juego = Ahorcado()
      juego.palabra_secreta = "perro"
      juego.intento("m")
      juego.intento("f")
      juego.intento("d")
      juego.intento("q")
      juego.intento("w")
      self.assertEqual(juego.se_termino_el_juego(), True)

if __name__=="__main__":
  unittest.main()       
