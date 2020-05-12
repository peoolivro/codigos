# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 05
# Questão.: 5.14.8
# Autor...: Fábio Procópio
# Data....: 15/06/2019

lin = int(input("Informe a quantidade de linhas da matriz: "))
col = int(input("Informe a quantidade de colunas da matriz: "))
M = []
if lin != col:
    print("Matriz não é quadrada. Portanto, não pode ser identidade.")
else:
    for i in range(lin):
        LINHA = []  # Inicia a inclusão de elementos na linha i
        for j in range(col):
            elem = int(input("M[%d][%d]= " % (i + 1, j + 1)))
            # Inclui elemento digitado na lista LINHA, que corresponde à linha i
            LINHA.append(elem)
        print()
        M.append(LINHA)  # Adiciona elementos digitados na linha i

    identidade = True  # Considera que a matriz é I
    for i in range(lin):
        for j in range(col):
            if i == j:  # Elemento está na diagonal principal (DP)?
                if M[i][j] != 1:  # É diferente de 1?
                    identidade = False  # Matriz não é identidade
                    break
            else:
                if M[i][j] != 0:  # É diferente de 0?
                    identidade = False  # Matriz não é identidade
                    break

    for i in range(lin):
        linha = ""
        for j in range(col):
            linha += str(M[i][j]) + " "
        print(linha)

    if identidade:
        print("\nM é uma matriz identidade.")
    else:
        print("\nM não é uma matriz identidade.")
