from elitismo import selecionar_elite


populacao = [
    ["Amigo1", "Amigo2", "Amigo3"],
    ["Amigo3", "Amigo1", "Amigo2"],
    ["Amigo2", "Amigo3", "Amigo1"],
    ["Amigo1", "Amigo3", "Amigo2"],
    ["Amigo2", "Amigo1", "Amigo3"]
]


fitnesses = [
    0.10,
    0.80,
    0.30,
    0.50,
    0.20
]


elite = selecionar_elite(
    populacao,
    fitnesses,
    2
)


print("População:")

for i, cromossomo in enumerate(populacao, start=1):
    print(f"Indivíduo {i}: {cromossomo} | Fitness: {fitnesses[i - 1]}")


print()
print("Elite:")

for cromossomo in elite:
    print(cromossomo)