# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: Exercício Proposto 1
# Autor...: Fábio Procópio
# Data....: 15/06/2019

termo1    = int(input("Informe o 1º termo da P.A.: "))
num_termo = int(input("Informe o número de termos da P.A.: "))
razao     = int(input("Informe a razão da P.A.: "))
PA        = [termo1]

termo_anterior = termo1
print(f"***** {num_termo} primeiros termos da P.A. *****")
for x in range(num_termo - 1):
   termo_atual    = termo_anterior + razao
   PA.append(termo_atual)
   termo_anterior = termo_atual
print(PA)
print("*" * 38)
soma = sum(PA)
print(f"Soma dos elementos da PA = {soma}")
