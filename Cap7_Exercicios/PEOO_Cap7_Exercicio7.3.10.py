# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.10
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

cadastro = obtem_dados_funcionarios()
sexo = input("Digite seu sexo: ")
media = retorna_media_salarial(sexo, cadastro)

if sexo.upper() == "F":
  print("Média salarial das mulheres: R$ {:.2f}".format(media))
elif sexo.upper() == "M":
  print("Média salarial dos homens: R$ {:.2f}".format(media))
else:
  print('ERRO: sexo correspondente não encontrado.')
