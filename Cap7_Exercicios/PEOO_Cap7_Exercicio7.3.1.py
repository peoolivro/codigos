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
    print(f'Área do círculo: {area:.2f}')
elif escolha == 2:
    base = float(input('Informe a base: '))
    altura = float(input('Informe a altura: '))
    area = calcula_area_triangulo(base, altura)
    print(f'Área do triângulo: {area:.2f}')
elif escolha == 3:
    base = float(input('Informe a base: '))
    altura = float(input('Informe a altura: '))
    area = calcula_area_retangulo(base, altura)
    print(f'Área do retângulo: {area:.2f}')
else:
    print('ERRO: não foi possível encontrar a figura informada.')
