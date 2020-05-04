# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.8
# Autor...: Givanaldo Rocha de Souza
# Data....: 02/05/2020

from classes import ContaInvestimento

conta = ContaInvestimento(1000.0, 10)
print("Saldo inicial: R$ %.2f" % conta.saldo)
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
conta.adicionarJuros()
print("Após 5 rodadas de juros...")
print("Saldo resultante: R$ %.2f" % conta.saldo)