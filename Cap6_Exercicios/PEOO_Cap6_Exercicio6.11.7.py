# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.7
# Autor...: Fábio Procópio
# Data....: 03/06/2019

series = {}
while True:
   serie = input("\nSérie: ")
   ator1 = input("  Ator 1: ")
   ator2 = input("  Ator 2: ")
   series.update({serie: [ator1, ator2]})
   resp = input("Deseja continuar [S|N]? ")
   if resp == "n" or resp == "N":
      print("\n")    
      break
	
serie = input("Informe o nome de uma série: ")
if serie in series: 
    print("Atores: {} e {}\n".format(series.get(serie)[0], series.get(serie)[1]))
else:
    print("Série não cadastrada.")
    
