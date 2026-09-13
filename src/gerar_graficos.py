import os
import matplotlib.pyplot as plt

from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from algoritmo_genetico import algoritmo_genetico

SEED = 2024105231940012

os.makedirs("resultados", exist_ok=True)


# EXPERIMENTO A
N = 8

amigos = gerar_amigos(N, SEED)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

_, _, historico_A = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=50,
    geracoes=300,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

plt.figure(figsize=(10, 5))

plt.plot(
    range(1, len(historico_A) + 1),
    historico_A
)

plt.xlabel("Geração")
plt.ylabel("Melhor custo")
plt.title("Convergência do Algoritmo Genético - Experimento A")
plt.grid()

plt.savefig(
    "resultados/experimento_A.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# EXPERIMENTO B
N = 15

amigos = gerar_amigos(N, SEED)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

_, _, historico_B = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=100,
    geracoes=500,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

plt.figure(figsize=(10, 5))

plt.plot(
    range(1, len(historico_B) + 1),
    historico_B
)

plt.xlabel("Geração")
plt.ylabel("Melhor custo")
plt.title("Convergência do Algoritmo Genético - Experimento B")
plt.grid()

plt.savefig(
    "resultados/experimento_B.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráficos gerados com sucesso!")