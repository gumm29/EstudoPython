from Animal import Animal

class Cachorro(Animal):
  def __init__(self, nome='Floki', altura=20):
    self._nome = nome
    self._altura = altura
