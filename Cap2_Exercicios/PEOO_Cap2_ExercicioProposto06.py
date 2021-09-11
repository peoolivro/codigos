# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 02
# Questão.: Exercício Proposto 6
# Autor...: Fábio Procópio
# Data....: 18/02/2019

print("Uma equação do 2º grau tem a seguinte estrutura:\nax^2 + bx + c = 0\n")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

print(f"Delta = {delta:.2f}")
