# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 02
# Questão.: 2.8.10
# Autor...: Fábio Procópio
# Data....: 18/02/2019

copo1 = "laranja"
copo2 = "acerola"

print("Antes da troca")
print("Copo1 tem {}".format(copo1))
print("Copo2 tem {}".format(copo2))

copo1, copo2 = copo2, copo1

print("\nDepois da troca")
print("Copo1 tem {}".format(copo1))
print("Copo2 tem {}".format(copo2))
