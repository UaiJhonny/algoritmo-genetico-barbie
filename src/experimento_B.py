import random
import time

from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from algoritmo_genetico import algoritmo_genetico

SEED = 2024105231940012
N = 15

print("=== EXPERIMENTO B ===")
print()

random.seed(SEED)

amigos = gerar_amigos(
    N,
    SEED
)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

print("Quantidade de amigos:", N)
print()

print("Amigos:")
for nome, posicao in amigos.items():
    print(nome, ":", posicao)

print()

inicio = time.perf_counter()

melhor_ag, custo_ag, historico = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=100,
    geracoes=500,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

tempo_ag = time.perf_counter() - inicio

ultima_melhoria = 0

for i in range(1, len(historico)):
    if historico[i] < historico[i - 1]:
        ultima_melhoria = i + 1

print("=== RESULTADOS ===")
print()

print("Melhor rota:")
print(melhor_ag)

print()

print("Melhor custo:", custo_ag)
print("Tempo:", tempo_ag, "segundos")
print("Última melhoria na geração:", ultima_melhoria)

print()

print("Comparação com força bruta:")
print("15! =", 1307674368000)
print("Quantidade de rotas possíveis:", 1307674368000)
print("Força bruta seria inviável para este experimento.")