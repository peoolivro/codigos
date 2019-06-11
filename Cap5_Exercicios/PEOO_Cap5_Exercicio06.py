#Capítulo 05, questão 06
import random
from random import randrange

N = int(input("Digite um valor N (tal que N > 1): "))
if N > 1:
   #Gera uma lista aleatória com N elementos, dentro do intervalo [1, 10]	
   L = [randrange(1, 11) for i in range(N)]
   print("Lista: ", L)
   produto_elementos = 1
   for num in L:
       produto_elementos *= num
   media_geo = produto_elementos ** (1 / N)
   print("Média geométrica da lista: {:.2f}".format(media_geo))   
else:
    print("Valor informado deve ser maior que 1.")


