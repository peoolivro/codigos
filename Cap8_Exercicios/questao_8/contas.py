# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.8
# Autor...: Givanaldo Rocha de Souza
# Data....: 02/05/2020

class ContaInvestimento:
    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        self.saldo += (self.saldo * self.taxaJuros / 100)