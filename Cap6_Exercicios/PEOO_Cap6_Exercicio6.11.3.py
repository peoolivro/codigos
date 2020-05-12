# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.3
# Autor...: Fábio Procópio
# Data....: 03/06/2019

voos = {}
while True:
   numero = input("\nVoo: ")
   origem = input("Origem: ")
   dest   = input("Destino: ")
   
   voos.update({numero: [origem, dest]})
   resp = input("Deseja continuar [S|N]? ")
   if resp == "n" or resp == "N":
      print("\n")    
      break

voos_NAT = 0
for trecho in voos.values():
    if trecho[0].upper() == "NATAL":
       voos_NAT += 1	

print(f"Voos provindos de Natal: {voos_NAT}")
