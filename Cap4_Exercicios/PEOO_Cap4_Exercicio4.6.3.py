# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.3
# Autor...: Fábio Procópio
# Data....: 04/06/2019

soma_preco = 0
# Leitura do primeiro medicamento
medicamento = input("Medicamento: ")
preco       = float(input("R$: "))
# Na primeira leitura, naturalmente, ele é o mais barato
mais_barato = medicamento
menor_preco = preco
# Acumula o preço do primeiro produto no somatório
soma_preco += preco

# Já que o primeiro produto foi informado, restam 4...
for x in range(4):
   medicamento = input("Medicamento: ")
   preco       = float(input("R$: "))
   if preco < menor_preco:
      menor_preco = preco
      mais_barato = medicamento
   soma_preco += preco

media = soma_preco / 5
print(f"{mais_barato} é o medicamento mais barato e custa R$ {menor_preco:.2f}.")
print(f"Média dos preços: R$ {media:.2f}.")
