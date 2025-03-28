

import numpy as np
import igraph as ig

# Função para entrada de dados
def entrada():
    # Coleta o nome/caminho do arquivo desejado para leitura e carrega a matriz
    arquivo = str(input("Digite o nome do arquivo com a matriz desejada: "))
    mat = np.loadtxt(arquivo)
    # Coleta as dimensões da matriz (linhas, colunas)
    dim = mat.shape
    return mat, dim, arquivo

# Função de saída de dados
def saida(mat, dim, arq):
    # Define o nome do arquivo com base no arquivo original e dimensões da matriz
    nomearq = f"{arq} {dim[0]} {dim[1]}.txt"
    # Cria o arquivo e escreve a matriz nele
    with open(nomearq, 'w') as file:
        file.write(f"{mat}")
    
    # Exibe informações na tela
    print("A matriz no arquivo " + arq + " tem " + str(dim[0]) + " linhas e " + str(dim[1]) + " colunas\n")
    print("A matriz foi salva no arquivo de nome " + nomearq)

# Função para gerar e salvar a imagem do grafo
def gera_grafo(mat):
    # Converte a matriz em uma lista e cria o grafo ponderado
    g = ig.Graph.Weighted_Adjacency(mat.tolist(), mode=ig.ADJ_UNDIRECTED, attr="weight")
    # Plota e salva a imagem do grafo em 'graph.png'
    ig.plot(g, "graph.png")
    print("Imagem do grafo salva em 'graph.png'")

# Chamada das funções
mat, dim, arq = entrada()
saida(mat, dim, arq)
gera_grafo(mat)
