# Livro.....: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo..: 07
# Autor.....: Fábio Procópio
# Data......: 24/06/2019
# Comentário: Este arquivo contém todas as funções dos exercícios propostos do capítulo

# Funções da questão 01
def calcula_area_circulo(raio):
    return 3.14 * pow(raio, 2)

def calcula_area_triagulo(base, altura):
    return (base * altura) / 2

def calcula_area_retangulo(base, altura):
    return base * altura


# Funções da questão 02
def gera_matriz_aleatoria(linhas, colunas, inicio, fim):
   from random import randrange
   import random

   A = [[randrange(inicio, fim + 1) for i in range(colunas)]
        for j in range(linhas)]

   return A

def calcula_traco(A):
   linhas  = len(A)
   colunas = len(A[1])
   
   if linhas == colunas:
      ordem = len(A)
      traco = 0
      for i in range(ordem):
          traco += A[i][i] 

      return traco

   ''' Função só chegará neste ponto se número de linhas
   for diferente do número de colunas'''
   return "ERRO: Matriz não é quadrada. Não existe traço!" 

# Função da questão 03
def soma_matrizes(A, B):
   linhasA  = len(A)
   colunasA = len(A[1])
   linhasB  = len(B)
   colunasB = len(B[1])

   if linhasA == linhasB and colunasA == colunasB:
      # Cria C, uma matriz nula, de mesma ordem de A e de B. O objetivo é ter 
      # uma matriz com a mesma ordem das outras duas para executar a operação de soma.
      C = gera_matriz_aleatoria(linhasA, colunasA, 0, 0)
      for i in range(linhasA):
          for j in range(colunasA):
              # Atualiza a matriz C com os respectivos valores de A e de B
              C[i][j] = A[i][j] + B[i][j] 

      return C

   ''' Função só chegará neste ponto se número de linhas
   for diferente do número de colunas'''
   return "ERRO: A e B não possuem ordem iguais."

# Função da questão 04
def multipla_matriz_por_constante(k, A):
   linhas  = len(A)
   colunas = len(A[1]) 
   for i in range(linhas):
       for j in range(colunas):
           # Multiplica cada elemento de A pela constante k
           A[i][j] = k * A[i][j] 

   return A

# Função da questão 05
def ordena_series(series):
    ordenacao = {}
    for serie, atores in sorted(series.items()):
        atores.sort()
        ordenacao.update({serie: atores})
    return ordenacao
	
# Função da questão 06
def obtem_dados_funcionarios():
   funcionarios = {1: ['Ana', 'F', 'TI', 7, 3200],
                   2: ['Beatriz', 'F', 'TI', 4, 3720],
                   3: ['Carla', 'F', 'TI', 1, 2100],
                   4: ['Daniela','F', 'RH', 2, 3920],
	   	   5: ['Emílio','M', 'RH', 7, 4235.12],
		   6: ['Fernando','M', 'Marketing', 7, 1200],
		   7: ['Gabriela','F', 'Marketing', 8, 7234.89],
		   8: ['Hernandes','M', 'TI', 6, 4234.12],
		   9: ['Ítalo','M', 'RH', 13, 13934.23],
		   10: ['Janaína','F', 'RH', 7, 9341.89]}
   return funcionarios

# Função da questão 07
def retorna_qtde_homens_mulheres(cadastro):
    homens   = 0
    mulheres = 0
    for mat, dados in cadastro.items():
        # Índice com o sexo do funcionário
        if dados[1] == "M":
            homens += 1
        elif dados[1] == "F":
            mulheres += 1

    return homens, mulheres

# Função da questão 08
def retorna_funcionarios_maior5anos(cadastro):
    qtde_maior5anos = 0
    for dados in cadastro.values():
        # Índice com o tempo de serviço do funcionário
        if dados[3] > 5:
            qtde_maior5anos += 1
        
    return qtde_maior5anos

# Função da questão 09
def lista_mulheres_por_setor(cadastro, setor):
    mulheres_setor = {}
    for mat, dados in cadastro.items():
        # Índices com o sexo e o setor do funcionário
        if dados[1] == "F" and dados[2] == setor:
            mulheres_setor.update({mat: dados})
        
    return mulheres_setor

# Função da questão 10
def retorna_media_salarial_por_sexo(cadastro, sexo):
    soma_salarios = 0
    registros     = 0
    for mat, dados in cadastro.items():
        # Índice com o sexo do funcionário
        if dados[1] == sexo:
            soma_salarios += dados[4]
            registros += 1

    if registros > 0:        
       return soma_salarios / registros

    # Só chegará nesta linha se nenhum registro for encontrado
    return 0



    


    

