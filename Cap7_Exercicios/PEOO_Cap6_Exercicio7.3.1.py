# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 
# Autor...: Fábio Procópio
# Data....: 26/06/2019

from PEOO_Cap7_MinhasFuncoes import calcula_area_circulo, calcula_area_triagulo, calcula_area_retangulo

print("Cálculo das áreas de figuras geométricas:")
print("1. Círculo")
print("2. Triângulo")
print("3. Retângulo")

while True:
   op = int(input("\nQual figura deseja calcular a área? ")) 
   if op < 1 or op > 3:
      print("ERRO: Opção inválida!")
   else:
      if op == 1:
         raio = float(input("Raio: "))  
         area = calcula_area_circulo(raio) 
         print("Ac = {:.2f}".format(area))
      elif op == 2:
         base   = float(input("Base..: "))  
         altura = float(input("Altura: "))
         area   = calcula_area_triagulo(base, altura) 
         print("At = {:.2f}".format(area))
      else:
         base   = float(input("Base..: "))  
         altura = float(input("Altura: "))
         area   = calcula_area_retangulo(base, altura) 
         print("Ar = {:.2f}".format(area))
      break







