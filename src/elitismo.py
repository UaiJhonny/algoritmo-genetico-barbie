def selecionar_elite(populacao, fitnesses, quantidade):
    indices = sorted(
        range(len(populacao)),
        key=lambda i: fitnesses[i],
        reverse=True
    )

    elite = []

    for i in indices[:quantidade]:
        elite.append(populacao[i].copy())

    return elite