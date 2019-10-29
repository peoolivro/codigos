# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais Operacionais
# Capítulo: 06
# Questão.: 6.11.4
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

voos_REC = []
for num_voo, trecho in voos.items():
    if trecho[1].upper() == "RECIFE":
       # Por que não usar a instrução voos.pop(num_voo)?
       # Não é possível remover elementos de um dicionário enquanto ele
       # estiver sendo percorrido
       voos_REC.append(num_voo)
       #voos.pop(num_voo)

for num_voo in voos_REC:
    voos.pop(num_voo)

if len(voos) > 0:	
   for num_voo, trecho in voos.items():
      print("Voo: {}".format(num_voo))
      print("Origem: {}".format(trecho[0]))
      print("Destino: {}\n".format(trecho[1]))
else:
   print("Não há voos cadastrados.")




         
