from gerar_amigos import gerar_amigos
from populacao import gerar_populacao


amigos = gerar_amigos(8, 12345)

nomes_amigos = list(amigos.keys())

populacao = gerar_populacao(
    nomes_amigos,
    50
)

print("Quantidade de cromossomos:", len(populacao))
print()

for i, cromossomo in enumerate(populacao[:5], start=1):
    print(f"Cromossomo {i}:", cromossomo)

print()

todos_validos = True

for cromossomo in populacao:

    if len(cromossomo) != 8:
        todos_validos = False

    if len(set(cromossomo)) != 8:
        todos_validos = False

print("Todos os cromossomos são válidos:", todos_validos)