# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: 5.14.2
# Autor...: Fábio Procópio
# Data....: 15/06/2019

ATLETA = []
TEMPO  = []

for x in range(7):
   nome  = input("Informe o nome do nadador: ")
   tempo = float(input("Informe o tempo do nadador: "))
   ATLETA.append(nome)
   TEMPO.append(tempo)

#Recupera o índice em que está o melhor tempo
indice_melhor = TEMPO.index(min(TEMPO))
#Recupera o índice em que está o pior tempo
indice_pior   = TEMPO.index(max(TEMPO))
media_tempos  = sum(TEMPO) / len(TEMPO)

print("{} tem o melhor tempo.".format(ATLETA[indice_melhor]))
print("{} tem o pior tempo.".format(ATLETA[indice_pior]))
print("Média dos tempos: {:.2f}s.".format(media_tempos))
