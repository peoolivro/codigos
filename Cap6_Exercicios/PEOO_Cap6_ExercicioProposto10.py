# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: Exercício Proposto 10
# Autor...: Fábio Procópio
# Data....: 03/06/2019

funcionarios = {1: ['Ana', 'F', 'TI', 7, 3200],
                2: ['Beatriz', 'F', 'TI', 4, 3720],
                3: ['Carla', 'F', 'TI', 1, 2100],
                4: ['Daniela','F', 'RH', 2, 3920],
				5: ['Emílio','M', 'RH', 7, 4235.12],
				6: ['Fernando','M', 'Marketing', 7, 1200],
				7: ['Gabriela','F', 'Marketing', 8, 7234.89],
				8: ['Hernandes','M', 'TI', 6, 4234.12],
				9: ['Ítalo','M', 'RH', 13, 13934.23],
				10: ['Janaína','F', 'RH', 7, 9341.89],}

for mat, dados in funcionarios.items():
   if dados[1] == "M" and dados[2] != "TI":
      print(f"Matrícula: {mat}")
      print(f"Nome.....: {dados[0]}")
      print(f"Sexo.....: {dados[1]}")
      print(f"Setor....: {dados[2]}")
      print(f"Tempo....: {dados[3]}")
      print(f"Salário..: R$ {dados[4]:.2f}\n")
	  
	
