# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 02
# Questão.: 2.8.9
# Autor...: Fábio Procópio
# Data....: 18/02/2019

from math import sqrt

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

cubo      = pow(num2, 3)
media_geo = sqrt(num1 * num2)

print(f"\nCubo de {num2} é {cubo}")
print(f"Média geométrica entre {num1} e {num2} é {media_geo:.2f}")
