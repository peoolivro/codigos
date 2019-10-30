# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.1
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

print('Cálculo das áreas de figuras geométricas:')
print('1. Círculo')
print('2. Triângulo')
print('3. Retângulo')
escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    raio = float(input('Informe o raio: '))
    area = calcula_area_circulo(raio)
    print('Área do círculo: {:.2f}'.format(area))
elif escolha == 2:
    base = float(input('Informe a base: '))
    altura = float(input('Informe a altura: '))
    area = calcula_area_triangulo(base, altura)
    print('Área do triângulo: {:.2f}'.format(area))
elif escolha == 3:
    base = float(input('Informe a base: '))
    altura = float(input('Informe a altura: '))
    area = calcula_area_retangulo(base, altura)
    print('Área do retângulo: {:.2f}'.format(area))
else:
    print('ERRO: não foi possível encontrar a figura informada.')
