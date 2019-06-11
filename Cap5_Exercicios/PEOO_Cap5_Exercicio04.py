#Capítulo 05, questão 04

N = int(input("Digite um número ímpar, maior que 1: "))
if N <= 1 or N % 2 == 0:
   print("Número informado não atende os critérios definidos.")
else:
   L = []
   for x in range(N):
       num = int(input("Digite um número maior ou igual a zero: "))
       L.append(num)

   '''Pega o índice central da lista. Observe a conversão para inteiro.
   Como a quantidade de elementos de L é ímpar, então a divisão por 2
   resultatá em algo x.5.'''
   centro = int(len(L) / 2)     
   elemento_central = L[centro] #Pega o elemento central da lista
   fatorial = 1 #1 é o valor que nunca alterará o produto
   for n in range(2, elemento_central + 1):
       fatorial *= n #fatorial = fatorial * n
   print("Lista: ", L)
   print("Portanto, {}! = {}".format(elemento_central, fatorial))
