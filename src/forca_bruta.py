from itertools import permutations


def forca_bruta(nomes_amigos, nomes, matriz):
    indices = {
        nome: i
        for i, nome in enumerate(nomes)
    }

    casa = indices["Casa"]

    melhor_cromossomo = None
    melhor_custo = float("inf")

    for permutacao in permutations(nomes_amigos):

        custo = matriz[casa][indices[permutacao[0]]]

        for i in range(len(permutacao) - 1):
            atual = indices[permutacao[i]]
            proximo = indices[permutacao[i + 1]]

            custo += matriz[atual][proximo]

        custo += matriz[indices[permutacao[-1]]][casa]

        if custo < melhor_custo:
            melhor_custo = custo
            melhor_cromossomo = list(permutacao)

    return melhor_cromossomo, melhor_custo