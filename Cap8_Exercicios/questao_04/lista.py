# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.4
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

class Lista():

    def __init__(self, itens):
        self.itens = itens

    def exibirListaDistinta(self):
        novaLista = []
        for item in self.itens:
            if item not in novaLista:
                novaLista.append(item)
        return novaLista

