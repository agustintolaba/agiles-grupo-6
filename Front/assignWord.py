import random
from typing import Self 

class Ahorcado: 
  def __init__(self,palabra):
    self.palabra_secreta = palabra
    self.vidas = 5
    self.letras_adivinadas = set()
    self.letras_incorrectas = set()
    self.palabra_a_mostrar = []
    self.partina_concluida = False
    

  def ingresa_palabra(self,palabra_secreta): 
    self.palabra_secreta= palabra_secreta
    return self.palabra_secreta   
  
 
  def informaCantidadDeLetrasDeLaPalabra(self,palabra_secreta: str) -> int:
  
    return len(palabra_secreta)

  def verificaLetraEnLaPalabra(self,palabra_secreta:str,letra:str)-> bool:

    return letra.lower() in palabra_secreta.lower()

  
  def arriesgaPalabra(self,palabra_secreta:str,palabra:str):

    if palabra.lower() == palabra_secreta.lower():
      return True
    else:
      return False
    
  def adivinando(self,palabra_secreta,letra):
    if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
      return #ya esta fue ingresada
    if self.verificaLetraEnLaPalabra(palabra_secreta,letra):
      self.letras_adivinadas.add(letra)
    else: 
      self.vidas-=1
      self.letras_incorrectas.add(letra)
    
  def ganado(self):
      return set(self.palabra_secreta).issubset(self.letras_adivinadas)
    
  def perdido(self):
    return self.vidas == 0
  
  def iniciar_juego(self, palabra):
        self.vidas = 5
        self.letras_adivinadas = set()
        self.partida_concluida = False
        self.letras_arriesgada = []
        self.vidas_restantes = 5
        self.palabra_secreta = palabra
        self.fin_juego()
        
       # self.long = len(self.palabra_a_adivinar[0])
        self.palabra_a_mostrar = ["_" for _ in self.palabra_secreta[0]]
       

  def fin_juego(self):
        if self.partida_concluida:
            if self.vidas_restantes == 0:
                url = "img/0.png"
                self.img = url.replace(" ", "")
            else:
                url = "img/Winner.jpg"
                self.img = url.replace(" ", "")
        else:
            self.img = ("img/ " + str(self.vidas_restantes) + ".png").replace(" ", "")

  def se_termino_el_juego(self):
        if self.vidas_restantes == 0 or (
            "".join(self.palabra_a_mostrar) == self.palabra_secreta[0]
        ):
            self.partida_concluida = True
            self.fin_juego()
        return self.partida_concluida