def get_int(mensagem):
  while True: 
    try:
      value = int(input(mensagem))
      return value
    except ValueError:
      print("Digite um numero inteiro")
      