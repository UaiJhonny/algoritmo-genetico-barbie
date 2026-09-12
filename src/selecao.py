import random


def selecao_roleta(populacao, fitnesses, tamanho):
    soma_fitness = sum(fitnesses)

    probabilidades = [
        fitness / soma_fitness
        for fitness in fitnesses
    ]

    acumuladas = []

    total = 0

    for probabilidade in probabilidades:
        total += probabilidade
        acumuladas.append(total)

    selecionados = []

    for _ in range(tamanho):
        sorteio = random.random()

        for i, limite in enumerate(acumuladas):
            if sorteio <= limite:
                selecionados.append(populacao[i])
                break

    return selecionados