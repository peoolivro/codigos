# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.10
# Autor...: Fábio Procópio
# Data....: 31/05/2019

print(f"{'*'*18} TABELA IMC {'*'*18}")
print("IMC                            Situação")
print("Abaixo de 18,5                 Abaixo do peso")
print("Acima de 18,5 e menor que 25   Peso normal")
print("A partir de 25 e menor que 30  Sobrepeso")
print("Acima de 30 e menor que 35     Obesidade grau 1")
print("Acima de 35 e menor que 40     Obesidade grau 2")
print("Acima de 40                    Obesidade grau 3")
print("*" * 48)
altura = float(input("Informe sua estatura (em metros): "))
peso = int(input("Informe seu peso (em Kg): "))
imc = peso / pow(altura, 2)

if imc < 18.5:
   print(f"Seu IMC é {imc:.2f} -> Abaixo do peso.")
elif 18.5 < imc < 25:
   print(f"Seu IMC é {imc:.2f} -> Peso normal.")  
elif 25 < imc < 30:
   print(f"Seu IMC é {imc:.2f} -> Sobrepeso.")
elif 30 < imc < 35:
   print(f"Seu IMC é {imc:.2f} -> Obesidade grau 1.")
elif 35 < imc < 40:
   print(f"Seu IMC é {imc:.2f} -> Obesidade grau 2.")
else:
   print(f"Seu IMC é {imc:.2f} -> Obesidade grau 3.")
