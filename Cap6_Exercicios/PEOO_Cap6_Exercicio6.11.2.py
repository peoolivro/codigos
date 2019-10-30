# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.2
# Autor...: Fábio Procópio
# Data....: 03/06/2019
from operator import itemgetter

clientes = {}
while True:
   razao   = input("\nNome: ")
   compras = float(input("Compras: R$ "))
   
   clientes.update({razao: compras})
   resp = input("Deseja continuar [S|N]? ")
   if resp == "n" or resp == "N":
      print("\n")    
      break

for razao, compras in sorted(clientes.items(), reverse = True, key=itemgetter(1)):
	print("{}: R$ {:.2f}".format(razao, compras))
