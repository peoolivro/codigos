# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.2
# Autor...: Fábio Procópio
# Data....: 04/06/2019

termo1    = int(input("Informe o 1º termo da P.A.: "))
num_termo = int(input("Informe o número de termos da P.A.: "))
razao     = int(input("Informe a razão da P.A.: "))

termo_anterior = termo1
print(f"***** {num_termo} primeiros termos da P.A. *****")
print(termo1)
for x in range(num_termo - 1):
   termo          = termo_anterior + razao
   print(termo)
   termo_anterior = termo
print("*" * 38)
