# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.8
# Autor...: Fábio Procópio
# Data....: 03/06/2019

produtos = {1: ['Monitor LED 24"', 599.99],
            2: ['Teclado wireless', 49.26],
            3: ['Mouse wireless', 19.9],
            4: ['Cartucho colorido', 54]}

for cod, prod in produtos.items():
   if prod[1] > 50:
      prod[0] += " (em promoção)"
      prod[1] *= 0.90
	
for cod, prod in produtos.items():
   print("Código: {}".format(cod))
   print("Nome..: {}".format(prod[0]))
   print("R$....: {:.2f}\n".format(prod[1]))
      
