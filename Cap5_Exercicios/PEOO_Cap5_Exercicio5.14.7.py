# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: 5.14.7
# Autor...: Fábio Procópio
# Data....: 15/06/2019

from random import randrange
import random

lin = int(input("Informe a quantidade de linhas da matriz: "))
col = int(input("Informe a quantidade de colunas da matriz: "))
M = [[randrange(0, 2) for i in range(col)]
                      for j in range(lin)]

# Se optar por não gera a matriz aleatoriamente, para testar o algoritmo
# crie uma matriz manualmente. A ordem da matriz será 3 x 3, independente da
# quantidade de linhas e de colunas que o usuário informar
# Remova o comentário da linha abaixo para criar uma matriz que não é nula:
# M = [[-2, 0, 0], [0, 0, 0], [0, 0, 0]]
# Remova o comentário da linha abaixo para criar uma matriz que é nula:
# M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

nula = True # Considera que a matriz é nula
for i in range(lin):
   for j in range(col):
      if M[i][j] != 0: # Elemento é diferente de 0?
         nula = False  # Matriz não é identidade
         break
      
for i in range(lin):
   linha = ""
   for j in range(col):
      linha += str(M[i][j]) + " "
   print(linha)
              
if nula:
   print("\nMatriz gerada é nula.")
else:
   print("\nMatriz gerada não é nula..")
