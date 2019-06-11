# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 2.8.9
# Autor...: Fábio Procópio
# Data....: 18/02/2019

from math import sqrt

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

cubo      = pow(num2, 3)
media_geo = sqrt(num1 * num2)

print("\nCubo de {} é {}".format(num2, cubo))
print("Média geométrica entre {} e {} é {:.2f}".format(num1, num2, media_geo))
