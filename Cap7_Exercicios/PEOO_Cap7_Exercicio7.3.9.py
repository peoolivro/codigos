# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.9
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *

cadastro = obtem_dados_funcionarios()

setor = input("Digite seu setor: ")
for nome1, dados1 in lista_mulheres_por_setor(cadastro, setor).items():
  print(nome1, dados1)
