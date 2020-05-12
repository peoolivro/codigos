# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 02
# Questão.: 2.8.5
# Autor...: Fábio Procópio
# Data....: 18/02/2019

from math import sqrt

print("Dados do ponto P1:")
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
print("Dados do ponto P2:")
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

d = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print(f"Distância entre P1 e P2 = {d:.2f}")
