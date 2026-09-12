from mapa import CASA_DA_BARBIE, POSICOES_AMIGOS
from matriz_custos import calcular_matriz_custos


nomes, matriz = calcular_matriz_custos(
    CASA_DA_BARBIE,
    POSICOES_AMIGOS
)


print("Matriz de custos:")
print()

print("        ", end="")

for nome in nomes:
    print(f"{nome:>10}", end="")

print()

for i, nome in enumerate(nomes):

    print(f"{nome:<10}", end="")

    for custo in matriz[i]:
        print(f"{custo:>10}", end="")

    print()