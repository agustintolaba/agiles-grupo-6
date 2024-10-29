import random
from typing import Self 

class Ahorcado: 
  def __init__(self,palabra):
    self.palabra_secreta = palabra
    self.vidas = 3
    self.letras_adivinadas = set()

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
    if letra in self.letras_adivinadas:
      return #ya esta adivinada
    if self.verificaLetraEnLaPalabra(palabra_secreta,letra):
      self.letras_adivinadas.add(letra)
    else: 
      self.vidas-=1
    
  def ganado(self):
      return set(self.palabra_secreta).issubset(self.letras_adivinadas)
    
  def perdido(self):
    return self.vidas == 0