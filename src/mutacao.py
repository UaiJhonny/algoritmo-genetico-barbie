import random


def mutacao_swap(cromossomo):
    mutado = cromossomo.copy()

    posicao1, posicao2 = random.sample(
        range(len(mutado)),
        2
    )

    mutado[posicao1], mutado[posicao2] = (
        mutado[posicao2],
        mutado[posicao1]
    )

    return mutado