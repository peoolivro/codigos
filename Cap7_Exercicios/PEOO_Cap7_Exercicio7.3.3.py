# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.3
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

linhas = int(input('Informe a quantidade de linhas da matriz: '))
colunas = int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial = int(input('Informe o intervalo inicial: '))
intervalo_final = int(input('Informe o intervalo final: '))

A = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
B = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
if len(A) == len(B) and len(A[0]) == len(B[0]):
    print(f'Matriz A = {A} \nMatriz B = {B} \nMatriz C (A+B) = {soma_matrizes(A,B)}')
else:
    print('ERRO: as matrizes não são de mesma ordem.')
