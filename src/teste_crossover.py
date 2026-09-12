from crossover import crossover_ox


pai1 = [
    "Amigo1",
    "Amigo2",
    "Amigo3",
    "Amigo4",
    "Amigo5",
    "Amigo6",
    "Amigo7",
    "Amigo8"
]

pai2 = [
    "Amigo5",
    "Amigo8",
    "Amigo2",
    "Amigo7",
    "Amigo1",
    "Amigo4",
    "Amigo6",
    "Amigo3"
]


filho = crossover_ox(pai1, pai2)


print("Pai 1:", pai1)
print("Pai 2:", pai2)
print("Filho :", filho)

print()

print("Tamanho correto:", len(filho) == 8)
print("Sem genes repetidos:", len(set(filho)) == 8)
print("Todos os amigos presentes:", set(filho) == set(pai1))