# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.10
# Autor...: Fábio Procópio
# Data....: 04/06/2019

aprovado    = 0
prova_final = 0
reprovado   = 0

num_alunos = 5
for i in range(num_alunos):
   N1 = float(input("\nNota 1: "))
   N2 = float(input("Nota 2: "))
   media = (N1 + N2) / 2
   
   if media >= 6:
      aprovado += 1
   elif media < 2:
      reprovado += 1
   else:
      prova_final += 1
                          
print(f"\nAprovados..: {((aprovado / num_alunos) * 100):.2f}")
print(f"Prova final: {((prova_final / num_alunos) * 100):.2f}")
print(f"Reprovados.: {((reprovado / num_alunos) * 100):.2f}")
