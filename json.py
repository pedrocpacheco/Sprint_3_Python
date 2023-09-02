import json

def customerByCpf(cpf):
  with open ("./customers.json") as file:
    data = json.load(file)
    for customer in data:
      if customer["cpf"] == cpf:
        return customer
  print("Customer not found")

def analystByRm(rm):
  with open ("./analyst.json") as file: 
    data = json.load(file)
    for analyst in data:
      if analyst["rm"] == rm:
        return analyst
  print("Analyst not Found")
  
def findInJson(credential, file):
  data = json.loaad(file)
  for person in data:
    if person["rm"] == credential or person["cpf"] == credential:
      return person
      
print("Retornando Customer:")   
print(customerByCpf("51670111162"))

print("Retornando Analyst: ")
print(analystByRm("RM9158167013"))
