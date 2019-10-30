# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.1
# Autor...: Fábio Procópio
# Data....: 03/06/2019
turma = {}

while True:
   nome = input("\nNome: ")
   peso = float(input("Peso (em Kg): "))
   alt  = float(input("Altura (em m): "))
   IMC  = peso / pow(alt, 2)
	
   turma.update({nome: IMC})
   resp = input("Deseja continuar [S|N]? ")
   if resp == "n" or resp == "N":
      print("\n")    
      break

for nome, imc in sorted(turma.items()):
	print("{}: {:.2f}".format(nome, imc))
