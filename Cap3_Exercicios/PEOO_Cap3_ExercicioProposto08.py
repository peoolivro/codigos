# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: Exercício Proposto 8
# Autor...: Fábio Procópio
# Data....: 31/05/2019

from math import sqrt

print("Uma equação do 2º grau tem o seguinte formato: ax^2+bx+c=0.")
a = float(input("Informe a: "))
b = float(input("Informe b: "))
c = float(input("Informe c: "))

delta = pow(b, 2) - 4 * a * c

if delta < 0:
   print("Não existem raízes reais.")
elif delta == 0:
   x = -b / (2 * a)
   print(f"x1 = x2 = {x:.2f}")
else:
   x1 = (-b + sqrt(delta)) / (2 * a)
   x2 = (-b - sqrt(delta)) / (2 * a)
   print(f"x1 = {x1:.2f}")
   print(f"x2 = {x2:.2f}")
