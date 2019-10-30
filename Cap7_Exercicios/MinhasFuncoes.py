# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 07
# Autor...: Emanuel Lázaro
# Data....: 29/10/2019
# Comentário: Este arquivo contém todas as funções dos exercícios propostos do Capítulo 07

#### Funções utilizadas na Questão 7.3.1 ####
from math import pi
def calcula_area_circulo(raio):
    return pi * raio**2

def calcula_area_triangulo(base, altura):
    return (base * altura)/2

def calcula_area_retangulo(base, altura):
    return base * altura
#############################################

#### Funções utilizadas na Questão 7.3.2 ####
def gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final):
    from random import randrange
    M = [[randrange(intervalo_inicial, intervalo_final) for i in range(colunas)]
          for j in range(linhas)]
    return M 
    
def calcula_traco_matriz(matriz):
    traco = []
    soma = 0 
    for i in range(len(matriz)):
        traco.append(matriz[i][soma])
        soma += 1
    return sum(traco)
#############################################

#### Funções utilizadas na Questão 7.3.3 ####
def soma_matrizes(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
                C[i].append(A[i][j]+B[i][j])
    return C
#############################################

#### Função utilizada na Questão 7.3.4 ####
def multiplica_matriz_por_constante(matriz, constante):
    matriz_resultante = []
    for i in range(len(matriz)):
        matriz_resultante.append([])
        for j in matriz[i]:
                matriz_resultante[i].append(j*constante)
    return matriz_resultante
###########################################

#### Função utilizada na Questão 7.3.5 ####
def series_protagonistas(dicionario):
        dicionario2 = {}
        for serie, protagonista in sorted(dicionario.items()):
            protagonista.sort()
            dicionario2.update({serie:protagonista})
        return dicionario2 
###########################################        
        
#### Função utilizada na Questão 7.3.6 ####
def obtem_dados_funcionarios():
  func = {1: ["Ana", "F", "TI", 7, 3200.00],
          2: ["Beatriz", "F", "TI", 4, 3720.00],
          3: ["Carla", "F", "TI", 1, 2100.00],
          4: ["Daniela", "F", "RH", 2, 3920.00],
          5: ["Emílio", "M", "RH",7, 4235.12],
          6: ["Fernando", "M", "Marketing", 7, 1200.00],
          7: ["Gabriela", "F", "Marketing", 8, 7234.89],
          8: ["Hernandes", "M", "TI", 6, 4234.12],
          9: ["Ítalo", "M", "RH", 13, 13934.23],
          10: ["Janaína", "F", "RH", 7, 9341.89]}
  return func
###########################################

#### Função utilizada na Questão 7.3.7 ####
def retorna_homens_mulheres(dicio_cadastro):
    h = 0
    m = 0
    for nome, dados in dicio_cadastro.items():
      print(nome, dados)
      if dados[1].upper() == "F":
         m += 1
      else:
         h += 1
    return "\nQuantidade de mulheres cadastradas: {} \nQuantidade de homens cadastrados: {}".format(m, h)
###########################################

#### Função utilizada na Questão 7.3.8 ####
def retorna_tempo_servico(dicionario): 
    lista_tempo = []
    dicio_novo = {}

    for nome, dados in dicionario.items():
        if dados[3] > 5:
           lista_tempo.append(nome)

    for numero in lista_tempo:
        dicio_novo.update({numero: dicionario.get(numero)})

    return dicio_novo
###########################################

#### Função utilizada na Questão 7.3.9 ####
def lista_mulheres_por_setor(cadastro, setor):
  lista_chaves = []
  dicio_novo = {}

  for nome, dados in cadastro.items():
    if dados[1] == "F" and dados[2].upper() == setor.upper():
      lista_chaves.append(nome)
  
  for chaves in lista_chaves:
    dicio_novo.update({chaves: cadastro.get(chaves)})

  return dicio_novo
###########################################

#### Função utilizada na Questão 7.3.10 #####
def retorna_media_salarial(sexo, cadastro): 
  lista_salarios = []
  for nome, dados in cadastro.items():
    if sexo.upper() == dados[1].upper():
       lista_salarios.append(dados[4])

  if len(lista_salarios) == 0:
     return 0
    
  return sum(lista_salarios)/len(lista_salarios)
#############################################





