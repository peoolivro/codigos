# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.7
# Autor...: Givanaldo Rocha de Souza
# Data....: 02/05/2020

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def abastecer(self,litros):
        self.combustivel += litros

    def exibirCombustivel(self):
        print('Combustível: %.1f litros' % self.combustivel)

    def andar(self, distancia):
        print("Carro andou %d Km" % distancia)
        litrosGastos = distancia / self.consumo
        self.combustivel -= litrosGastos