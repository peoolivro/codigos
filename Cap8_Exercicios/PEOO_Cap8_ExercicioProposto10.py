# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.10
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

# Como já existe a classe Ponto (questão 3), foi criada a classe PontoModificado para a questão 10
# Contudo, foi criado o alias (apelido) Ponto para simplificar a classe.
from classes import PontoModificado as Ponto

pA = Ponto("A", 100, 200)
pB = Ponto("B", 120, 150)
pC = Ponto("C",  50,  95)
pD = Ponto("D", 199,  54)

print(pA)
print(pB)
print(f"Distância entre {pA.nome} e {pB.nome}: {pA.distancia(pB):.2f} \n")

print(pA)
print(pD)
print(f"Distância entre {pA.nome} e {pD.nome}: {pA.distancia(pD):.2f} \n")

print(pB)
print(pC)
print(f"Distância entre {pB.nome} e {pC.nome}: {pB.distancia(pC):.2f} \n")
