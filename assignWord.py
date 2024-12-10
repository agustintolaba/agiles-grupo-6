import random
from typing import Self 

class Ahorcado: 
  def __init__(self):
    self.palabra_secreta = []
    self.palabra_vacia = ""
    self.vidas = 5
    self.vidas_restantes = 5
    self.letras_adivinadas = set()
    self.letras_incorrectas = set()
    self.palabra_a_mostrar = []
    self.partida_concluida = False
    self.img = ""
    self.letras_arriesgada = []
    

  def informaCantidadDeLetrasDeLaPalabra(self,palabra_secreta: str) -> int:
  
    return len(palabra_secreta)

  def verificaLetraEnLaPalabra(self,palabra_secreta:str,letra:str)-> bool:

    #return letra.lower() in palabra_secreta.lower()
    if letra.lower() in palabra_secreta.lower():
      self.letras_adivinadas.add(letra)
      return True
    else: 
      return False

  def letras_arriesgadas_en_el_juego(self, letra):
        if letra in self.letras_arriesgada:
            return True
        else:
            return False
        
  def arriesgaPalabra(self,palabra_secreta:str,palabra:str):

    if palabra.lower() == palabra_secreta.lower():
      return True
    else:
      self.vidas_restantes -=1
      if self.vidas_restantes == 10:
            self.partida_concluida = True
      return False
       
  def ganado(self):
      return set(self.palabra_secreta).issubset(self.letras_adivinadas)
    
  def perdido(self):
    return self.vidas == 0
  
  def iniciar_juego(self, palabra):
        self.vidas = 5
        self.letras_adivinadas = set()
        self.partida_concluida = False
        self.letras_incorrectas = set()
        self.vidas_restantes = 5
        self.palabra_secreta = palabra
        self.letras_arriesgada = []
        self.fin_juego()
        
        self.palabra_a_mostrar = ["_" for _ in self.palabra_secreta]
       

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
            "".join(self.palabra_a_mostrar) == self.palabra_secreta
        ):
            self.partida_concluida = True
            self.fin_juego()
        return self.partida_concluida
  
  def intentoP(self, palabraA):
        self.partida_concluida = True
        self.palabra_vacia = str(palabraA)
        if "".join(palabraA) == self.palabra_secreta[0]:
            self.palabra_a_mostrar = list(self.palabra_secreta[0])
        else:
            self.vidas_restantes = 0
            self.palabra_a_mostrar = list(palabraA)

  def intento(self, letra):
        
        if letra in self.letras_arriesgada:

            return False
        
        self.letras_arriesgada.append(letra)

        if self.verificaLetraEnLaPalabra(str(self.palabra_secreta),letra):
            
            self.mostrar_letra_correcta(letra)
            return True
        else:
            
            self.vidas_restantes -= 1
            self.img = ("static\img\ " + str(self.vidas_restantes) + ".png").replace(
                " ", ""
            )
        self.fin_juego()
        return False
        
  def mostrar_letra_correcta(self, letra):
        letras_adivinadas = []
        for l in self.palabra_secreta:
            if l == letra or l in self.letras_arriesgada:
                letras_adivinadas.append(l)
            else:
                letras_adivinadas.append("_")
        self.palabra_a_mostrar = letras_adivinadas

