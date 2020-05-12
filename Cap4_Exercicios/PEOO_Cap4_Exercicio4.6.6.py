# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.6
# Autor...: Fábio Procópio
# Data....: 04/06/2019

estatura = float(input("Estatura do aluno: "))

'''Como não há nenhuma estatura a ser comparada, neste momento, o primeiro
aluno tem a maior e a menor estatura'''
menor = estatura
maior = estatura

soma_estatura = 0
soma_estatura += estatura
cont = 1
while True:
    estatura = float(input("Estatura do aluno: "))
    if estatura < 0:  # Quando estatura menor que zero, laço será interrompido
        break

    if estatura < menor:
        menor = estatura
    elif estatura > maior:
        maior = estatura

    # Conta quantas estaturas foram informadas
    cont += 1
    # Acumula as estaturas informadas
    soma_estatura += estatura
    # cont e soma_estatura serão usadas para calcular a média

print(f"{maior}m é a maior estatura.")
print(f"{menor}m é a menor estatura.")
media = soma_estatura / cont
print(f"Média das estaturas = {media:.2f}m")
