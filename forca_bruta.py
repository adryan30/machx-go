# Implementação do algoritmo de força bruta
from itertools import *

def gerar_caminhos(matrix):
    # Extrai os nodos da matrix
    nodos = [node for node in range(len(matrix))]
    # Remove a última cidade para gerar permutações não cíclicos
    ultimo_nodo = nodos.pop()
    # Enumera todos os caminhos partindo dos nodos
    lista_permutacoes = list(permutations(nodos))
    # Controi uma árvore
    lista_arvore = list(map(list, lista_permutacoes))

    # Fechando os caminhos / Construindo os ciclos completos
    for caminho in lista_arvore:
        caminho.append(ultimo_nodo)
        caminho.append(caminho[0])

    return nodos, lista_arvore

def forca_bruta(matrix):
    # Gera todos os caminhos possiveis
    nodos, lista_arvore = gerar_caminhos(matrix)

    # Calcula o custo de cada ciclo
    lista_custo = []
    for ciclo in lista_arvore:
        # Inicializa o custo para cada ciclo
        custo_ciclo = 0
        # Converte dois nodos em um ciclo para um índice no array de entrada
        for index in range(0, (len(nodos) - 1)):
            # custo_ciclo é calculado a partir da matriz de entrada e entre
            # dois nodos em um ciclo
            custo_ciclo = custo_ciclo + matrix[ciclo[index]][ciclo[index+1]]
        lista_custo.append(custo_ciclo)

    # Calcula o ciclo de menor custo
    menor_custo = min(lista_custo)
    indice_menor_custo = lista_custo.index(menor_custo)
    matrix_saida = ["Força Bruta", menor_custo, lista_arvore[indice_menor_custo]]

    return matrix_saida


matrix = [[0, 8, 50, 31, 12, 48, 36, 2, 5, 39, 10],
          [8, 0, 38, 9, 33, 37, 22, 6, 4, 14, 32],
          [50, 38, 0, 11, 55, 1, 23, 46, 41, 17, 52],
          [31, 9, 11, 0, 44, 13, 16, 19, 25, 18, 42],
          [12, 33, 55, 44, 0, 54, 53, 30, 28, 45, 7],
          [48, 37, 1, 13, 54, 0, 26, 47, 40, 24, 51],
          [36, 22, 23, 16, 53, 26, 0, 29, 35, 34, 49],
          [2, 6, 46, 19, 30, 47, 29, 0, 3, 27, 15],
          [5, 4, 41, 25, 28, 40, 35, 3, 0, 20, 21],
          [39, 14, 17, 18, 45, 24, 34, 27, 20, 0, 43],
          [10, 32, 52, 42, 7, 51, 49, 15, 21, 43, 0]]

print(forca_bruta(matrix))

