# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.8
# Autor...: Fábio Procópio
# Data....: 04/06/2019

print(22 * "-")
print("Código   Cargo")
print(22 * "-")
print("1        Enfermeiro(a)")
print("2        Nutricionista")
print("3        Médico(a)")

qtde_nutricionista = 0
total_sal_nutricionista = 0
while True:   
   cargo = int(input("Informe um código: "))
   if cargo >= 1 and cargo <= 3:
      salario = float(input("Salário R$: "))
      if cargo == 2:
         qtde_nutricionista += 1
         total_sal_nutricionista += salario
      resp = input("Deseja continuar [S|N]? ")
      if resp.upper() == "N":
         break      
   else:
      print("Código inválido.")

media = 0
# Teste é realizado para garantir que não haverá divisão por zero
if qtde_nutricionista > 0:
   media = total_sal_nutricionista / qtde_nutricionista
   
print("Média salarial de nutricionistas: R$ {:.2f}".format(media))

   

   
