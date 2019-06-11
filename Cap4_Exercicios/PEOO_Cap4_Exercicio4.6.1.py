# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.1
# Autor...: Fábio Procópio
# Data....: 04/06/2019

a = int(input("Digite a: "))
b = int(input("Digite b: "))
if a < b:
   soma = 0
   for x in range(a, b + 1):
      soma += x
   print("Soma dos inteiros no intervalo [{}, {}] é {}.".format(a, b, soma))
else:
   print("ERRO: a deve ser maior que b.")
