from gerar_amigos import gerar_amigos


amigos = gerar_amigos(8, 12345)

print("Amigos sorteados:")

for nome, posicao in amigos.items():
    print(nome, ":", posicao)