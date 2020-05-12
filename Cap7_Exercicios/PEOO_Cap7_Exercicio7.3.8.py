# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 7.3.8
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019

from MinhasFuncoes import *
cadastro = obtem_dados_funcionarios()
for matricula, dados in retorna_tempo_serviço(cadastro).items():
  print(f"{matricula}: {dados}")

