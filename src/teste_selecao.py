from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from populacao import gerar_populacao
from avaliacao import calcular_custo_rota, calcular_fitness
from selecao import selecao_roleta


amigos = gerar_amigos(8, 12345)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())

populacao = gerar_populacao(
    nomes_amigos,
    50
)

fitnesses = []

for cromossomo in populacao:

    custo = calcular_custo_rota(
        cromossomo,
        nomes,
        matriz
    )

    fitness = calcular_fitness(custo)

    fitnesses.append(fitness)


selecionados = selecao_roleta(
    populacao,
    fitnesses,
    50
)


print("População original:", len(populacao))
print("População selecionada:", len(selecionados))

print()
print("Exemplos de indivíduos selecionados:")

for i, cromossomo in enumerate(selecionados[:5], start=1):
    print(f"Selecionado {i}:", cromossomo)