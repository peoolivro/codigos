# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: 5.14.10
# Autor...: Fábio Procópio
# Data....: 15/06/2019

from random import randrange
import random

lin = int(input("Informe a quantidade de linhas da matriz: "))
col = int(input("Informe a quantidade de colunas da matriz: "))
M = [[randrange(0, 2) for i in range(col)]
                      for j in range(lin)]

#Se optar por não gera a matriz aleatoriamente, para testar o algoritmo
#crie uma matriz manualmente.
#Remova o comentário da linha abaixo para criar uma matriz que não é esparsa:
#M = [[0, 0, 0], [0, 1, 5], [6, 7, 1]]
#Remova o comentário da linha abaixo para criar uma matriz que é esparsa:
#M = [[2, 0, 0], [0, 1, 0], [0, 2, 3]]

esparsa = True #Considera que a matriz é esparsa
qtdeZeros = 0
for i in range(lin):
   for j in range(col):
      if M[i][j] == 0:
         qtdeZeros += 1
         
for i in range(lin):
   linha = ""
   for j in range(col):
      linha += str(M[i][j]) + " "
   print(linha)
              
if qtdeZeros > (lin * col)/2:
   print("\nMatriz gerada é esparsa.")
else:
   print("\nMatriz gerada não é esparsa.")
      
