import random 

class Ahorcado: 
  def __init__(self):
    self.palabra_secreta=None

  def ingresa_palabra(self,palabra_secreta): 
    self.palabra_secreta= palabra_secreta
    return self.palabra_secreta   
  
  def informaCantidadDeLetrasDeLaPalabra(self,palabra_secreta: str) -> int:
  
    return len(palabra_secreta)

  def verificaLetraEnLaPalabra(self,palabra_secreta:str,letra:str)-> bool:

    return letra.lower() in palabra_secreta.lower()
