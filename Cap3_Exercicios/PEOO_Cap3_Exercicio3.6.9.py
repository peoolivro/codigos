# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 3.6.9
# Autor...: Fábio Procópio
# Data....: 31/05/2019

print("{} {} {}".format("*" * 14, "PROMOÇÃO BLACK FRIDAY", "*" * 15))
print("Código     Condição de Pagamento         Desconto(%)")
print("1          À vista (em espécie)                   15")
print("2          Cartão de débito                       10")
print("3          Cartão de crédito (vencimento)          5")
print("*" * 52)
valor = float(input("Valor R$: "))
opcao = int(input("Escolha uma opção: "))

if opcao < 1 or opcao > 3:
   print("Forma de pagamento inválida.")
elif opcao == 1:
   valor_final = valor * 0.85 #(100 - 15)/100 = 0.85 (15% de desconto)
   print("Valor final: R$ {:.2f}".format(valor_final))
elif opcao == 2:  
   valor_final = valor * 0.90 #(100 - 10)/100 = 0.90 (10% de desconto)
   print("Valor final: R$ {:.2f}".format(valor_final))
else:
   valor_final = valor * 0.95 #(100 - 95)/100 = 0.95 (5% de desconto)
   print("Valor final: R$ {:.2f}".format(valor_final))
