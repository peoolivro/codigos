# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 04
# Questão.: 4.6.9
# Autor...: Fábio Procópio
# Data....: 04/06/2019

print(22 * "-")
print("Código   Cargo")
print(22 * "-")
print("1        Enfermeiro(a)")
print("2        Nutricionista")
print("3        Médico(a)")

qtde_medico_sal_maior_4500 = 0
while True:   
   cargo = int(input("Informe um código: "))
   if cargo >= 1 and cargo <= 3:
      salario = float(input("Salário R$: "))
      if cargo == 3 and salario > 4500:
         qtde_medico_sal_maior_4500 += 1
      resp = input("Deseja continuar [S|N]? ")
      if resp.upper() == "N":
         break      
   else:
      print("Código inválido.")
   
print(f"Médicos com salários superiores a R$ 4.500,00: {qtde_medico_sal_maior_4500}")
