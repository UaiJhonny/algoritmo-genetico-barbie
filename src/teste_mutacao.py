from mutacao import mutacao_swap


cromossomo = [
    "Amigo1",
    "Amigo2",
    "Amigo3",
    "Amigo4",
    "Amigo5",
    "Amigo6",
    "Amigo7",
    "Amigo8"
]


mutado = mutacao_swap(cromossomo)


print("Original:", cromossomo)
print("Mutado:  ", mutado)

print()

print("Tamanho correto:", len(mutado) == 8)
print("Sem genes repetidos:", len(set(mutado)) == 8)
print("Mesmos amigos:", set(mutado) == set(cromossomo))
print("Original preservado:", cromossomo != mutado)