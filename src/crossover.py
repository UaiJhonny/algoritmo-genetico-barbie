import random


def crossover_ox(pai1, pai2):
    tamanho = len(pai1)

    inicio, fim = sorted(
        random.sample(range(tamanho), 2)
    )

    filho = [None] * tamanho

    filho[inicio:fim + 1] = pai1[inicio:fim + 1]

    posicao = (fim + 1) % tamanho

    for gene in pai2:

        if gene not in filho:

            filho[posicao] = gene

            posicao = (posicao + 1) % tamanho

    return filho