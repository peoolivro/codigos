# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 06
# Questão.: 6.11.9
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
   if dados[1] == "F" and dados[2] == "TI" and dados[4] > 3000:
      print("Matrícula: {}".format(mat))
      print("Nome.....: {}".format(dados[0]))
      print("Sexo.....: {}".format(dados[1]))
      print("Setor....: {}".format(dados[2]))
      print("Tempo....: {}".format(dados[3]))
      print("Salário..: R$ {:.2f}\n".format(dados[4]))
	  
	
