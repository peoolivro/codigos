# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 09
# Questão.: 9.4.1
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

class Ingresso:
    def __init__(self, evento, valor):
        self.evento = evento
        self.valor = valor

    def exibirValor(self):
        return self.valor

    def __str__(self):
        return ("%s: R$ %.2f" % (self.evento, self.valor))