from mapa import CASA_DA_BARBIE, POSICOES_AMIGOS
from astar import a_estrela


inicio = CASA_DA_BARBIE
objetivo = POSICOES_AMIGOS["Suzy"]

caminho, custo = a_estrela(inicio, objetivo)

print("Casa:", inicio)
print("Suzy:", objetivo)
print("Custo:", custo)
print("Quantidade de posições:", len(caminho))
