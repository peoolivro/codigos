# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: Exercício Proposto 7
# Autor...: Fábio Procópio
# Data....: 31/05/2019

altura1 = float(input("Digite a estatura da 1ª pessoa (em metros): "))
altura2 = float(input("Digite a estatura da 2ª pessoa (em metros): "))
altura3 = float(input("Digite a estatura da 3ª pessoa (em metros): "))

if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
   print("\nHá, pelo menos, 2 números iguais")
elif altura1 > altura2 and altura1 > altura3:
   print(f"A pessoa mais alta tem {altura1}m.")
elif altura2 > altura1 and altura2 > altura3:
   print(f"A pessoa mais alta tem {altura2}m.")    
else:
   print(f"A pessoa mais alta tem {altura3}m.")
