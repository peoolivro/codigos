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
   print(f"\nMédia ponderada calculada: {media:.2f}.")
elif op == 2:
   quadrado = (num1 + num2) ** 2
   print(f"\nQuadrado da soma dos números: {quadrado:.2f}.")      
else:
   if num1 < num2:      
      cubo = num1 ** 3
      print(f"\n{num1:.2f} é menor número e o seu cubo é {cubo:.2f}.")
   else:
      cubo = num2 ** 3
      print(f"\n{num2:.2f} é menor número e o seu cubo é {cubo:.2f}.")   
   
         
