# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: Exercício Proposto 1
# Autor...: Fábio Procópio
# Data....: 04/06/2019

a = int(input("Digite a: "))
b = int(input("Digite b: "))
if a < b:
   soma = 0
   for x in range(a, b + 1):
      soma += x
   print(f"Soma dos inteiros no intervalo [{a}, {b}] é {soma}.")
else:
   print("ERRO: a deve ser maior que b.")
