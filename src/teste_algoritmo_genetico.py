from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from algoritmo_genetico import algoritmo_genetico


random_seed = 12345

amigos = gerar_amigos(
    8,
    random_seed
)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

melhor_cromossomo, melhor_custo, historico = algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=50,
    geracoes=300,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
)

print("Melhor rota encontrada:")
print(melhor_cromossomo)

print()
print("Melhor custo:", melhor_custo)
print("Quantidade de gerações:", len(historico))
print("Custo na primeira geração:", historico[0])
print("Custo na última geração:", historico[-1])