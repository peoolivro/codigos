# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.3
# Autor...: Fábio Procópio
# Data....: 31/05/2019


print("**** TABELA VERDADE ****")
print("1. Operador AND")
print("2. Operador OR")
print("3. Operador NOT")
opcao = int(input("Escolha uma opção: "))

if opcao < 1 or opcao > 3:
    print("Opção inválida.")
elif opcao == 3:
    operador = int(input("Informe um bit: "))
    print(f"NOT {operador} = {not (operador)}")
else:
    operador1 = int(input("Informe o primeiro bit: "))
    operador2 = int(input("Informe o segundo bit: "))
    if opcao == 1:
        print(f"{operador1} AND {operador2} = {operador1 and operador2}")
    else:
        print(f"{operador1} OR {operador2} = {operador1 or operador2}")
