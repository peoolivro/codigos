# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Questão.: 
# Autor...: Fábio Procópio
# Data....: 26/06/2019

from PEOO_Cap7_MinhasFuncoes import ordena_series

series = {"O Mecanismo": ["Otto Jr.", "Carol Abras"],
          "How to get away with murder": ["Viola Davis", "Bily Brown"]
         }


print("**** Antes da ordenação ****")
for serie, atores in series.items():
    print("Série: {}".format(serie))
    print("  Atores: {} e {}\n".format(atores[0], atores[1]))

print("\n**** Depois da ordenação ****")
series = ordena_series(series)
for serie, atores in sorted(series.items()):
    print("Série: {}".format(serie))
    print("  Atores: {} e {}\n".format(atores[0], atores[1]))
