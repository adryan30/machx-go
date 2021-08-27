# Implementação do algoritmo de força bruta
from itertools import permutations
from timeit import default_timer as timer


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
    matrix_saida = ["Força Bruta", menor_custo,
                    lista_arvore[indice_menor_custo]]

    return matrix_saida


matrix = [[0, 300, 352, 466, 217, 238, 431, 336, 451,  47, 415, 515, ],
          [300,   0, 638, 180, 595, 190, 138, 271, 229, 236, 214, 393, ],
          [352, 638,   0, 251,  88, 401, 189, 386, 565, 206, 292, 349, ],
          [466, 180, 251,   0, 139, 371, 169, 316, 180, 284, 206, 198, ],
          [217, 595,  88, 139,   0, 310, 211, 295, 474, 130, 133, 165, ],
          [238, 190, 401, 371, 310,   0, 202, 122, 378, 157, 362, 542, ],
          [431, 138, 189, 169, 211, 202,   0, 183,  67, 268, 117, 369, ],
          [336, 271, 386, 316, 295, 122, 183,   0, 483, 155, 448, 108, ],
          [451, 229, 565, 180, 474, 378,  67, 483,   0, 299, 246, 418, ],
          [47, 236, 206, 284, 130, 157, 268, 155, 299,   0, 202, 327, ],
          [415, 214, 292, 206, 133, 362, 117, 448, 246, 202,   0, 394, ],
          [515, 393, 349, 198, 165, 542, 368, 108, 418, 327, 394,   0, ]]


start = timer()
resultado = forca_bruta(matrix)
end = timer()
print(resultado)
print(f'{end - start}s')
