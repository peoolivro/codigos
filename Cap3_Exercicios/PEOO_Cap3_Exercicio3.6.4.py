# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.4
# Autor...: Fábio Procópio
# Data....: 31/05/2019

login = input("Login: ")
senha = input("Senha: ")

if (login == "procopio" and senha == "12345") or (login == "paiva" and senha == "54321"):
   print("Seja bem vindo!")
else:
   print("Usuário e senha não conferem.")
