#Capítulo 05, questão 09
from random import randrange
import random

lin = int(input("Informe a quantidade de linhas da matriz: "))
col = int(input("Informe a quantidade de colunas da matriz: "))
M = [[randrange(1, 11) for i in range(col)]
                       for j in range(lin)]

#Se optar por não gera a matriz aleatoriamente, para testar o algoritmo
#crie uma matriz manualmente.
#Remova o comentário da linha abaixo para criar uma matriz que não é diagonal:
#M = [[1, 2, 3], [4, 1, 5], [6, 7, 1]]
#Remova o comentário da linha abaixo para criar uma matriz que é diagonal:
#M = [[2, 0, 0], [0, 1, 0], [0, 0, 3]]

diagonal = True #Considera que a matriz é diagonal
for i in range(lin):
   for j in range(col):
      #Elemento não está na DP e é diferente de 0?
      if i != j and M[i][j] != 0: 
         diagonal = False  #Matriz não é diagonal
         break
      
for i in range(lin):
   linha = ""
   for j in range(col):
      linha += str(M[i][j]) + " "
   print(linha)
              
if diagonal:
   print("\nMatriz gerada é diagonal.")
else:
   print("\nMatriz gerada não é diagonal.")
      
