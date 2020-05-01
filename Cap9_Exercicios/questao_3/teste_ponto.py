# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 09
# Questão.: 9.4.3
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

from ponto import Ponto

pontos = []

pontos.append(Ponto("A", 100, 200))
pontos.append(Ponto("B", 120, 150))
pontos.append(Ponto("C",  50,  95))
pontos.append(Ponto("D", 199,  54))

for p in pontos:
    print(p)