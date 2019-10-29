# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: 5.14.5
# Autor...: Fábio Procópio
# Data....: 15/06/2019

from math import sqrt

L = [9, 3, 5, 7, 2, 1]
menor = min(L)
maior = max(L)
media_geo = sqrt(menor * maior)
print("Lista: ", L)
print("Média geométrica entre {} e {} = {}.".format(menor, maior, media_geo))
