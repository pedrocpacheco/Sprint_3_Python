import utils

class Menu():
  def __init__(self):
    self.options = [
      {
        "action": "",
        "description": "Cadastrar-se como Ciclista"
      },
      {
        "action": "",
        "description": "Enviar fotos da sua bicicleta"
      },
      {
        "action": "",
        "description": "Analisar Bicicleta"
      },
    ]
        
  def show_options(self):
    for index, option in enumerate(self.options, 1):
      print(f"{index} - {option['description']}")

    print("Caso queira encerrar o programa, a qualquer momento pressione CTRL + C")

  def get_opition(self):
    while True:
      option = utils.get_int("Selecione a opção desejada: ")
      if option:
        break
      print("Digite um numero inteiro")
    
    if option > len(self.option):
      print("Digite um numero maior que 0 ")



menu = Menu()
menu.show_options()