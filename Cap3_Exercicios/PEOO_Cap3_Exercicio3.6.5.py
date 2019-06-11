# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.5
# Autor...: Fábio Procópio
# Data....: 31/05/2019

print("-*" * 20)
print("1. Programador de Sistemas")
print("2. Analista de Sistemas")
print("3. Analista de Banco de Dados")
print("-*" * 20)
salario = float(input("Digite o salário do funcionário: R$ "))
cargo   = int(input("Digite o cargo do funcionário: "))
if cargo < 1 or cargo > 3:
   print("Cargo inválido.")
elif cargo == 1:
   '''Acréscimo de 30% sobre o salário atual. Mesmo que:
         salario = salario * 1.3 ou
         salario = salario + salario * 0.3'''
   salario *= 1.3
   print("Novo salário: R$ {:.2f}".format(salario))
elif cargo == 2:
   '''Acréscimo de 30% sobre o salário atual. Mesmo que:
         salario = salario * 1.2 ou
         salario = salario + salario * 0.2'''
   salario *= 1.2
   print("Novo salário: R$ {:.2f}".format(salario))
else:
   '''Acréscimo de 30% sobre o salário atual. Mesmo que:
         salario = salario * 1.15 ou
         salario = salario + salario * 0.15'''
   salario *= 1.15
   print("Novo salário: R$ {:.2f}".format(salario))


