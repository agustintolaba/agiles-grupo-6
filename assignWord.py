import random 

class Ahorcado: 
  def __init__(self, palabras):
    self.palabras=palabras
    self.palabra_secreta=None

  def asignar_palabra(self): 
    self.palabra_secreta=random.choice(self.palabras)
    return self.palabra_secreta   
  
