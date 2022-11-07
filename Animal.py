class Animal:
  def __init__(self, nome, altura):
    self._nome = nome
    self._altura = altura

  @property #getter
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property #getter
  def altura(self):
    return self._altura

  @altura.setter
  def altura(self, altura):
    self.altura_ = altura