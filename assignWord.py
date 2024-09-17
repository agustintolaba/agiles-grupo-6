import random 

class Ahorcado: 
  def __init__(self):
    self.palabra_secreta=None

  def ingresa_palabra(self,palabra): 
    self.palabra_secreta= palabra
    return self.palabra_secreta   
  

