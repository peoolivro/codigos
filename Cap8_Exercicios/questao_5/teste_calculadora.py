# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.5
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

from calculadora import Calculadora

calc = Calculadora(2, 10)

print("%d + %d = %d" % (calc.op1, calc.op2, calc.somar()))
print("%d - %d = %d" % (calc.op1, calc.op2, calc.subtrair()))
print("%d * %d = %d" % (calc.op1, calc.op2, calc.multiplicar()))
print("%d / %d = %.2f" % (calc.op1, calc.op2, calc.dividir()))
print("%d elevado a %d = %d" % (calc.op1, calc.op2, calc.potencia()))
