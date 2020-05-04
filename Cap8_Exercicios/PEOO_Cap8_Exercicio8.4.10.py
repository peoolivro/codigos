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
print("Distância entre %s e %s: %.2f \n" % (pA.nome, pB.nome, pA.distancia(pB)))

print(pA)
print(pD)
print("Distância entre %s e %s: %.2f \n" % (pA.nome, pD.nome, pA.distancia(pD)))

print(pB)
print(pC)
print("Distância entre %s e %s: %.2f \n" % (pB.nome, pC.nome, pB.distancia(pC)))
