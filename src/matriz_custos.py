from astar import a_estrela


def calcular_matriz_custos(casa, amigos):
    pontos = [("Casa", casa)]

    for nome, posicao in amigos.items():
        pontos.append((nome, posicao))

    n = len(pontos)

    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if i == j:
                continue

            _, custo = a_estrela(
                pontos[i][1],
                pontos[j][1]
            )

            matriz[i][j] = custo

    nomes = [nome for nome, _ in pontos]

    return nomes, matriz