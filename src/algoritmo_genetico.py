import random

from populacao import gerar_populacao
from avaliacao import calcular_custo_rota, calcular_fitness
from selecao import selecao_roleta
from crossover import crossover_ox
from mutacao import mutacao_swap
from elitismo import selecionar_elite


def algoritmo_genetico(
    nomes_amigos,
    nomes,
    matriz,
    tamanho_populacao=50,
    geracoes=300,
    taxa_crossover=0.8,
    taxa_mutacao=0.03,
    tamanho_elite=2
):

    populacao = gerar_populacao(
        nomes_amigos,
        tamanho_populacao
    )

    melhor_cromossomo = None
    melhor_custo = float("inf")

    historico = []

    for geracao in range(geracoes):

        fitnesses = []
        custos = []

        for cromossomo in populacao:

            custo = calcular_custo_rota(
                cromossomo,
                nomes,
                matriz
            )

            fitness = calcular_fitness(custo)

            custos.append(custo)
            fitnesses.append(fitness)

            if custo < melhor_custo:
                melhor_custo = custo
                melhor_cromossomo = cromossomo.copy()

        historico.append(melhor_custo)

        elite = selecionar_elite(
            populacao,
            fitnesses,
            tamanho_elite
        )

        selecionados = selecao_roleta(
            populacao,
            fitnesses,
            tamanho_populacao
        )

        nova_populacao = elite.copy()

        while len(nova_populacao) < tamanho_populacao:

            pai1 = random.choice(selecionados)
            pai2 = random.choice(selecionados)

            if random.random() < taxa_crossover:
                filho = crossover_ox(pai1, pai2)
            else:
                filho = pai1.copy()

            if random.random() < taxa_mutacao:
                filho = mutacao_swap(filho)

            nova_populacao.append(filho)

        populacao = nova_populacao

    return melhor_cromossomo, melhor_custo, historico