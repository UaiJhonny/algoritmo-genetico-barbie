def calcular_custo_rota(cromossomo, nomes, matriz):
    indices = {
        nome: i
        for i, nome in enumerate(nomes)
    }

    custo = 0

    casa = indices["Casa"]

    primeiro = indices[cromossomo[0]]
    custo += matriz[casa][primeiro]

    for i in range(len(cromossomo) - 1):
        atual = indices[cromossomo[i]]
        proximo = indices[cromossomo[i + 1]]

        custo += matriz[atual][proximo]

    ultimo = indices[cromossomo[-1]]
    custo += matriz[ultimo][casa]

    return custo


def calcular_fitness(custo):
    return 1 / (1 + custo)