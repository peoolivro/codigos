# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: Exercício Proposto 3
# Autor...: Fábio Procópio
# Data....: 15/06/2019

import random

RIFA = []
while True:
    nome = input("Informe um nome: ")
    RIFA.append(nome)
    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break

random.shuffle(RIFA)  # Embaralha a lista
sorteado = random.choice(RIFA)  # Sorteia aleatoriamente um elemento
print(f"{sorteado} foi o(a) sorteado(a)!")
