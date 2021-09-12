# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: Exercício Proposto 1
# Autor...: Fábio Procópio
# Data....: 31/05/2019

num = int(input("Digite um número: "))
if num % 2 == 0:
    quadrado = num ** 2
    print(f"{num} é par e o seu quadrado é {quadrado}.")
else:
    cubo = num ** 3
    print(f"{num} é ímpar e o seu cubo é {cubo}.")
