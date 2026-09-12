import random


def gerar_cromossomo(nomes_amigos):
    return random.sample(nomes_amigos, len(nomes_amigos))


def gerar_populacao(nomes_amigos, tamanho):
    populacao = []

    for _ in range(tamanho):
        cromossomo = gerar_cromossomo(nomes_amigos)
        populacao.append(cromossomo)

    return populacao