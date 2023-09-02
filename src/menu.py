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

menu = Menu()

menu.show_options()
