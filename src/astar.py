import heapq

from mapa import (
    MAPA_TEXTO,
    LINHAS,
    COLUNAS,
    CUSTOS,
    BLOQUEADO
)


def heuristica(a, b):
    """
    Distância de Manhattan multiplicada pelo menor custo possível.
    """

    menor_custo = min(CUSTOS.values())

    return (
        abs(a[0] - b[0]) +
        abs(a[1] - b[1])
    ) * menor_custo


def vizinhos(pos):
    """
    Gera os vizinhos válidos de uma posição:
    cima, baixo, esquerda e direita.
    """

    r, c = pos

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):

        nr, nc = r + dr, c + dc

        if 0 <= nr < LINHAS and 0 <= nc < COLUNAS:

            terreno = MAPA_TEXTO[nr][nc]

            if terreno != BLOQUEADO:
                yield (nr, nc), CUSTOS[terreno]


def a_estrela(inicio, objetivo):
    """
    Busca A* entre duas posições quaisquer do mapa.

    Retorna:
        caminho: lista de posições
        custo_total: custo do caminho

    Se não existir caminho:
        (None, infinito)
    """

    if inicio == objetivo:
        return [inicio], 0

    contador = 0

    fronteira = [
        (heuristica(inicio, objetivo), 0, contador, inicio)
    ]

    veio_de = {
        inicio: None
    }

    custo_g = {
        inicio: 0
    }

    visitados = set()

    while fronteira:

        f, g, _, atual = heapq.heappop(fronteira)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == objetivo:

            caminho = []

            n = atual

            while n is not None:
                caminho.append(n)
                n = veio_de[n]

            caminho.reverse()

            return caminho, g

        for vizinho, custo in vizinhos(atual):

            novo_g = g + custo

            if novo_g < custo_g.get(vizinho, float("inf")):

                custo_g[vizinho] = novo_g

                veio_de[vizinho] = atual

                contador += 1

                heapq.heappush(
                    fronteira,
                    (
                        novo_g + heuristica(vizinho, objetivo),
                        novo_g,
                        contador,
                        vizinho
                    )
                )

    return None, float("inf")
