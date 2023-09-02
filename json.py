import json

def customerByCpf(cpf):
  with open ("./customers.json") as file:
    data = json.load(file)
    for customer in data:
      if customer["cpf"] == cpf:
        return customer
  print("Customer not found")
      
print("Retornando Customer:")   
print(customerByCpf("51670111162"))
