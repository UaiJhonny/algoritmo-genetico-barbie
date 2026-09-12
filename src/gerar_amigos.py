import random

from mapa import MAPA_TEXTO, LINHAS, COLUNAS, BLOQUEADO


def gerar_amigos(n, seed):
    random.seed(seed)

    posicoes_validas = []

    for r in range(LINHAS):
        for c in range(COLUNAS):
            if MAPA_TEXTO[r][c] != BLOQUEADO:
                posicoes_validas.append((r, c))

    escolhidas = random.sample(posicoes_validas, n)

    amigos = {}

    for i, posicao in enumerate(escolhidas, start=1):
        amigos[f"Amigo{i}"] = posicao

    return amigos