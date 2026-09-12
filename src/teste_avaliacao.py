from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from avaliacao import calcular_custo_rota, calcular_fitness


amigos = gerar_amigos(8, 12345)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

cromossomo = list(amigos.keys())

custo = calcular_custo_rota(
    cromossomo,
    nomes,
    matriz
)

fitness = calcular_fitness(custo)

print("Amigos:")
print(cromossomo)

print()
print("Custo da rota:", custo)
print("Fitness:", fitness)