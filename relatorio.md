# Relatório — Algoritmo Genético para o Problema da Barbie

## 1. Objetivo

O objetivo deste trabalho é utilizar um Algoritmo Genético (AG) para determinar uma ordem de visita aos amigos da Barbie, de forma que o custo total do percurso seja minimizado. A rota começa na casa da Barbie, passa por todos os amigos e retorna à casa.

Os custos reais entre os pontos foram obtidos utilizando o algoritmo A* desenvolvido no Trabalho 1. Esses valores foram armazenados em uma matriz de custos, utilizada posteriormente pelo Algoritmo Genético.

## 2. Configuração do Algoritmo Genético

Foram utilizados os seguintes parâmetros:

- Seleção: roleta;
- Crossover: Order Crossover (OX);
- Taxa de crossover: 80%;
- Mutação: swap;
- Taxa de mutação: 3%;
- Elitismo: 2 indivíduos;
- Semente aleatória: 2024105231940012.

No Experimento A foi utilizada uma população de 50 indivíduos e 300 gerações.

No Experimento B foi utilizada uma população de 100 indivíduos e 500 gerações.

## 3. Experimento A — 8 amigos

Para o primeiro experimento foram utilizados 8 amigos.

Como existem 8! = 40.320 possíveis ordens de visita, foi possível comparar o resultado do Algoritmo Genético com uma solução obtida por força bruta.

O Algoritmo Genético encontrou a rota:

Amigo4 → Amigo2 → Amigo6 → Amigo3 → Amigo1 → Amigo8 → Amigo7 → Amigo5

O custo obtido foi 302.

A força bruta também encontrou o custo ótimo de 302 e a mesma rota.

O Algoritmo Genético encontrou a solução ótima na geração 72.

### Comparação

| Método | Melhor custo | Tempo aproximado |
|---|---:|---:|
| Algoritmo Genético | 302 | 0,097 s |
| Força Bruta | 302 | 0,050 s |

Nesse experimento, o Algoritmo Genético conseguiu encontrar a solução ótima. A força bruta apresentou um tempo menor porque o número de possibilidades ainda é relativamente pequeno.

O gráfico de convergência pode ser observado em `resultados/experimento_A.png`.

## 4. Experimento B — 15 amigos

No segundo experimento foram utilizados 15 amigos.

O Algoritmo Genético foi executado com população de 100 indivíduos durante 500 gerações.

A melhor rota encontrada foi:

Amigo12 → Amigo14 → Amigo8 → Amigo1 → Amigo3 → Amigo6 → Amigo2 → Amigo4 → Amigo13 → Amigo9 → Amigo11 → Amigo5 → Amigo10 → Amigo7 → Amigo15

O melhor custo encontrado foi 431.

A última melhoria registrada ocorreu na geração 429 e o tempo de execução foi aproximadamente 0,68 segundo.

Para 15 amigos existem:

15! = 1.307.674.368.000

possíveis ordens de visita.

Esse número torna a busca por força bruta inviável na prática, pois seria necessário avaliar uma quantidade extremamente grande de rotas. Por isso, neste experimento foi utilizado somente o Algoritmo Genético.

O gráfico de convergência pode ser observado em `resultados/experimento_B.png`.

## 5. Conclusão

Os experimentos mostram que o Algoritmo Genético consegue encontrar boas soluções para o problema de ordenação das visitas.

No Experimento A, com 8 amigos, foi possível verificar a qualidade da solução comparando o AG com a força bruta. O AG encontrou exatamente a solução ótima, com custo 302.

No Experimento B, com 15 amigos, a quantidade de possibilidades aumentou para aproximadamente 1,3 trilhão de rotas, tornando a força bruta impraticável. Nesse cenário, o Algoritmo Genético encontrou uma solução com custo 431 em aproximadamente 0,68 segundo.

Os gráficos de convergência mostram que o custo diminui ao longo das gerações e tende a se estabilizar, indicando que o algoritmo está encontrando soluções cada vez melhores.