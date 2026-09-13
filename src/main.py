import random

from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from algoritmo_genetico import algoritmo_genetico

SEED = 2024105231940012
N = 8

random.seed(SEED)

amigos = gerar_amigos(N, SEED)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

melhor_rota, melhor_custo, historico = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=50,
    geracoes=300,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

print("=== ALGORITMO GENÉTICO - PROBLEMA DA BARBIE ===")
print()
print("Quantidade de amigos:", N)
print("Melhor rota:", melhor_rota)
print("Melhor custo:", melhor_custo)
print("Gerações:", len(historico))