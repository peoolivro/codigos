# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: Exercício Proposto 6
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

from classes import Funcionario

joao = Funcionario("João da Silva", 2350.0)
alex = Funcionario("Alex Torquato", 5000.0)

print(f"Salário de {joao.nome}: R$ {joao.salario:.2f}")
print(f"Aumento de 20%%: R$ {joao.aumentarSalario(20):.2f}")

print(f"\nSalário de {alex.nome}: R$ {alex.salario:.2f}")
print(f"Aumento de 50%%: R$ {alex.aumentarSalario(50):.2f}")
