# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.6
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentagem):
        return self.salario + (self.salario * porcentagem / 100)