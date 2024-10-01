import random 

class Ahorcado: 
  def __init__(self):
    self.palabra_secreta=None

  def ingresa_palabra(self,palabra_secreta): 
    self.palabra_secreta= palabra_secreta
    return self.palabra_secreta   
  
  def informaCantidadDeLetrasDeLaPalabra(self,palabra_secreta: str):
    #Return 0
    return len(self.palabra_secreta)
