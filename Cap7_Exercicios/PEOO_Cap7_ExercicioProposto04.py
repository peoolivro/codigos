# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: Exercício Proposto 4
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

linhas = int(input('Informe a quantidade de linhas da matriz: '))
colunas = int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial = int(input('Informe o intervalo inicial: '))
intervalo_final = int(input('Informe o intervalo final: '))

matriz = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
constante = int(input('Informe a constante que multiplicará a matriz gerada: '))
print(f'Matriz gerada: {matriz} \nMatriz C (k * A): {multiplica_matriz_por_constante(matriz, constante)}')
