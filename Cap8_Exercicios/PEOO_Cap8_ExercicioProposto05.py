# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: Exercício Proposto 5
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

from classes import Calculadora

calc = Calculadora(2, 10)

print(f"{calc.op1} + {calc.op2} = {calc.somar()}")
print(f"{calc.op1} - {calc.op2} = {calc.subtrair()}")
print(f"{calc.op1} * {calc.op2} = {calc.multiplicar()}")
print(f"{calc.op1} / {calc.op2} = {calc.dividir():.2f}")
print(f"{calc.op1} elevado a {calc.op2} = {calc.potencia()}")
