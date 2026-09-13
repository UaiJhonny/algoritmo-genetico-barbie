import random
import time

from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from algoritmo_genetico import algoritmo_genetico
from forca_bruta import forca_bruta


SEED = 2024105231940012
N = 8


print("=== EXPERIMENTO A ===")
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


print("Amigos:")
for nome, posicao in amigos.items():
    print(nome, ":", posicao)

print()


inicio = time.perf_counter()

melhor_ag, custo_ag, historico = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=50,
    geracoes=300,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

tempo_ag = time.perf_counter() - inicio


inicio = time.perf_counter()

melhor_bruta, custo_bruta = forca_bruta(
    nomes_amigos,
    nomes,
    matriz
)

tempo_bruta = time.perf_counter() - inicio


geracao_otima = None

for i, custo in enumerate(historico, start=1):
    if custo == custo_bruta:
        geracao_otima = i
        break


print("=== RESULTADOS ===")
print()

print("AG:")
print("Melhor rota:", melhor_ag)
print("Melhor custo:", custo_ag)
print("Tempo:", tempo_ag, "segundos")

print()

print("Força Bruta:")
print("Melhor rota:", melhor_bruta)
print("Custo ótimo:", custo_bruta)
print("Tempo:", tempo_bruta, "segundos")

print()

print("Comparação:")
print("AG encontrou o ótimo:", custo_ag == custo_bruta)

if geracao_otima is not None:
    print("Geração em que o AG encontrou o ótimo:", geracao_otima)
else:
    print("O AG não encontrou o ótimo durante as 300 gerações.")