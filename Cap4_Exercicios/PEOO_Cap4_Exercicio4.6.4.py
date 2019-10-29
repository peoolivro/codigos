# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.4
# Autor...: Fábio Procópio
# Data....: 04/06/2019

erros = 0
while erros < 3:
   senha = int(input("Senha: "))
   if senha == 123456:
      print("Olá, você. Seja bem-vindo ao nosso banco!")
      break
   else:
      # Houve erro
      erros += 1
      #Ainda há tentativas
      if erros < 3:
         #O comando "3 - erros" significa 3 tentativas - a quantidade de erros
         print("Senha incorreta! Você ainda tem {} tentativa(s).".format(3 - erros))
      else:
         print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixa.")
         break
      
