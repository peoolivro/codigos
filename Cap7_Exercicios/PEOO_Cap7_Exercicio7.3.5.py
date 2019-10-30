# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.5
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

series_person = {}
while True:
    serie = input('Informe o nome de uma série: ')
    prot1 = input('Informe o nome do 1º protagonista de {}: '.format(serie))
    prot2 = input('Informe o nome do 2º protagonista de {}: '.format(serie))
    series_person.update({serie:[prot1, prot2]})
    resp = input('Deseja continuar [S/N]? ')
    if resp.upper() == 'N':
        break
    
print('Dicionário original: ')
for serie, prot in series_person.items():
    print('Protagonista de {}: {} e {}'.format(serie, prot[0], prot[1]))

print('\nDicionário ordenado alfabeticamente: ')
for serie, prot in series_protagonistas(series_person).items():
    print('Protagonista de {}: {} e {}'.format(serie, prot[0], prot[1]))
