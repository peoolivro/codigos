# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais Operacionais
# Capítulo: 06
# Questão.: 6.11.6
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
	
for serie, atores in sorted(series.items()):
    atores = sorted(atores)
    print("Série: {}".format(serie))
    print("  Atores: {} e {}\n".format(atores[0], atores[1]))
    
