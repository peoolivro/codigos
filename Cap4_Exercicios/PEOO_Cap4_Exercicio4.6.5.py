# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.5
# Autor...: Fábio Procópio
# Data....: 04/06/2019

nome  = input("Nadador 1: ")
tempo = float(input("Tempo do nadador 1: "))

'''Como não há nenhum tempo a ser comparado, neste momento, o primeiro
nadador tem o melhor e o pior tempo ;-)'''
melhor_nadador = nome
melhor_tempo   = tempo 
pior_nadador   = nome
pior_tempo     = tempo

#Adiciona o tempo do primeiro nadador no somatório para calcular a média dos tempos
soma_tempo     = 0
soma_tempo     += tempo
tempo_12_15s   = 0
#Verifica se tempo do primeiro nadador deve ser considerado na contagem
if 12 <= tempo <= 15:
   tempo_12_15s += 1

for nadador in range(2, 8):
   '''str(nadador) converte o valor da variável nadador para string e concatena
   com a string Nadador. Para usuário aparecerá algo como "Nadador 2:" '''
   nome  = input("Nadador " + str(nadador) + ": ")
   tempo = float(input("Tempo do nadador " + str(nadador) + ": "))

   if tempo < melhor_tempo: # Tempo informado é menor do que o melhor tempo?
      melhor_nadador = nome # O melhor nadador passa a ser o atual
      melhor_tempo   = tempo# O melhor tempo passa a ser o atual 
   elif tempo > pior_tempo: # Tempo informado é maior do que o melhor tempo?
      pior_nadador   = nome # O pior nadador passa a ser o atual
      pior_tempo     = tempo# O pior tempo passa a ser o atual

   # Acumula o tempo atual
   soma_tempo += tempo
   
   # Tempo atual está dentro do intervalo [12, 15]?
   if 12 <= tempo <= 15:
      tempo_12_15s += 1

print("{} é o melhor nadador com {} seg.".format(melhor_nadador, melhor_tempo))
print("{} é o pior nadador com {} seg.".format(pior_nadador, pior_tempo))
media = soma_tempo / 7
print("Média dos tempos = {:.2f} seg.".format(media))
print("Atletas entre 12 seg e 15 seg: {}".format(tempo_12_15s))

      
