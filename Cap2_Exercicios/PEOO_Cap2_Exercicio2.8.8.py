# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 2.8.8
# Autor...: Fábio Procópio
# Data....: 18/02/2019

sal_minimo   = float(input("Informe o valor do salário mínimo atual (R$): "))
sal_usuario  = float(input("Informe o valor do seu salário mensal (R$): "))
qtd_salarios = sal_usuario / sal_minimo

print("Você recebe aproximadamente {:.2f} salário(s) mínimo(s).".format(qtd_salarios))
