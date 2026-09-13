import time

from mapa import CASA_DA_BARBIE
from gerar_amigos import gerar_amigos
from matriz_custos import calcular_matriz_custos
from forca_bruta import forca_bruta


amigos = gerar_amigos(
    8,
    12345
)

nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    amigos
)

nomes_amigos = list(amigos.keys())


inicio = time.perf_counter()

melhor_cromossomo, melhor_custo = forca_bruta(
    nomes_amigos,
    nomes,
    matriz
)

fim = time.perf_counter()

tempo = fim - inicio


print("Melhor rota:")
print(melhor_cromossomo)

print()
print("Custo ótimo:", melhor_custo)
print("Tempo da força bruta:", tempo, "segundos")