# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.7
# Autor...: Fábio Procópio
# Data....: 04/06/2019

idade = int(input("Idade: "))

'''Como não há nenhuma idade a ser comparada, neste momento, a primeira idade
é, ao mesmo tempo, o mais novo e o mais velho'''
mais_novo  = idade 
mais_velho = idade

while True:   
   idade = int(input("Idade: "))
   if idade < 0: #Quando idade negativa, laço será interrompido
      break
                          
   if idade < mais_novo:   
      mais_novo = idade
   elif idade > mais_velho:
      mais_velho = idade

print(f"Menor idade: {mais_novo}")
print(f"Maior idade: {mais_velho}")
media = (mais_novo + mais_velho) / 2
print(f"Média das duas idades = {media:.2f}")
