# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.2
# Autor...: Fábio Procópio
# Data....: 31/05/2019

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print("\n1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
op = int(input("Escolha uma opção: "))

if op < 1 or op > 3:
   print("\nOpção inválida.")
elif op == 1:
   media = (num1 * 2 + num2 * 3) / 5
   print("\nMédia ponderada calculada: {:.2f}.".format(media))
elif op == 2:
   quadrado = (num1 + num2) ** 2
   print("\nQuadrado da soma dos números: {:.2f}.".format(quadrado))      
else:
   if num1 < num2:      
      cubo = num1 ** 3
      print("\n{:.2f} é menor número e o seu cubo é {:.2f}.".format(num1, cubo))
   else:
      cubo = num2 ** 3
      print("\n{:.2f} é menor número e o seu cubo é {:.2f}.".format(num2, cubo))   
   
         
