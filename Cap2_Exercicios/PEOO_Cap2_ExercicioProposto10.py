# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 02
# Questão.: Exercício Proposto 10
# Autor...: Fábio Procópio
# Data....: 18/02/2019

copo1 = "laranja"
copo2 = "acerola"

print("Antes da troca")
print(f"Copo1 tem {copo1}")
print(f"Copo2 tem {copo2}")

copo1, copo2 = copo2, copo1

print("\nDepois da troca")
print(f"Copo1 tem {copo1}")
print(f"Copo2 tem {copo2}")
