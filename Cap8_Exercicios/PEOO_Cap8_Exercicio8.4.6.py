# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.6
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

from classes import Funcionario

joao = Funcionario("João da Silva", 2350.0)
alex = Funcionario("Alex Torquato", 5000.0)

print(("Salário de %s: R$ %.2f" % (joao.nome, joao.salario)))
print(("Aumento de 20%%: R$ %.2f" % (joao.aumentarSalario(20))))

print(("\nSalário de %s: R$ %.2f" % (alex.nome, alex.salario)))
print(("Aumento de 50%%: R$ %.2f" % (alex.aumentarSalario(50))))