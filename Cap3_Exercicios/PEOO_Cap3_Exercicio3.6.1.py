# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.1
# Autor...: Fábio Procópio
# Data....: 31/05/2019

num = int(input("Digite um número: "))
if num %2 == 0:
   quadrado = num ** 2
   print("{} é par e o seu quadrado é {}.".format(num, quadrado))
else:
   cubo = num ** 3
   print("{} é ímpar e o seu cubo é {}.".format(num, cubo))
