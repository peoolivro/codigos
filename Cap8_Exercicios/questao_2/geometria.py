# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.2
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return 2 * self.largura + 2 * self.altura

    def calcularArea(self):
        return self.largura * self.altura