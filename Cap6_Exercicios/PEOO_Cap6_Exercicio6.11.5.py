# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais Operacionais
# Capítulo: 06
# Questão.: 6.11.5
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

voo = input("Qual voo deseja alterar? ")
origem = input("Nova origem: ")
dest   = input("Novo destino: ")
if voo in voos:
   voos.update({numero: [origem, dest]})
   print("Voo alterado com sucesso.\n")
	
   for num_voo, trecho in voos.items():
      print("Voo: {}".format(num_voo))
      print("Origem: {}".format(trecho[0]))
      print("Destino: {}\n".format(trecho[1]))
else:
   print("Voo não cadastrado.")
