# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.2
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

linhas = int(input('Informe a quantidade de linhas da matriz: '))
colunas = int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial = int(input('Informe o intervalo inicial: '))
intervalo_final = int(input('Informe o intervalo final: '))

M = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
print(f'Matriz gerada: {M}')

if len(M) == len(M[0]):
    print(f'Traço da matriz gerada: {calcula_traco_matriz(M)}')

else:
    print('Não foi possível calcular o traço pois M não é quadrada.')
