# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: Exercício Proposto 7
# Autor...: Givanaldo Rocha de Souza
# Data....: 02/05/2020

from classes import Carro

meuCarro = Carro(12);           # consumo de 12 km/l
meuCarro.abastecer(40);         # abastece com 40 litros
meuCarro.exibirCombustivel()    # Imprime o combustível que resta no tanque.
meuCarro.andar(160);            # anda 160 quilômetros.
meuCarro.exibirCombustivel()
meuCarro.andar(280);            # anda 280 quilômetros.
meuCarro.exibirCombustivel()