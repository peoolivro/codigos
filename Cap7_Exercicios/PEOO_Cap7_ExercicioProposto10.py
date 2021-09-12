# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: Exercício Proposto 10
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

cadastro = obtem_dados_funcionarios()
sexo = input("Digite seu sexo: ")
media = retorna_media_salarial(sexo, cadastro)

if sexo.upper() == "F":
  print(f"Média salarial das mulheres: R$ {media:.2f}")
elif sexo.upper() == "M":
  print(f"Média salarial dos homens: R$ {media:.2f}")
else:
  print('ERRO: sexo correspondente não encontrado.')
