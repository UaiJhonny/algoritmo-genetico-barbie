# Relatório — Algoritmo Genético para o Problema da Barbie

## 1. Objetivo

O objetivo deste trabalho é utilizar um Algoritmo Genético (AG) para determinar uma ordem de visita aos amigos da Barbie, de forma que o custo total do percurso seja minimizado. A rota começa na casa da Barbie, passa por todos os amigos e retorna à casa.

Os custos reais entre os pontos foram obtidos utilizando o algoritmo A* desenvolvido no Trabalho 1. Esses valores foram armazenados em uma matriz de custos, utilizada posteriormente pelo Algoritmo Genético.

Para garantir a reprodução dos experimentos, foi utilizada como semente a matrícula:

`2024105231940012`

## 2. Configuração do Algoritmo Genético

Foram utilizados os seguintes parâmetros:

- Seleção: roleta;
- Crossover: Order Crossover (OX);
- Taxa de crossover: 80%;
- Mutação: swap;
- Taxa de mutação: 3%;
- Elitismo: 2 indivíduos;
- Semente aleatória: `2024105231940012`.

No Experimento A foi utilizada uma população de 50 indivíduos e 300 gerações.

No Experimento B foi utilizada uma população de 100 indivíduos e 500 gerações.

A matriz de custos foi calculada previamente utilizando o A*. Durante a execução do Algoritmo Genético, os custos das rotas foram obtidos somente por consultas à matriz, sem executar novamente o A*.

## 3. Experimento A — 8 amigos

Para o primeiro experimento foram utilizados 8 amigos.

Como existem:

`8! = 40.320`

possíveis ordens de visita, foi possível comparar o resultado do Algoritmo Genético com uma solução obtida por força bruta.

O Algoritmo Genético encontrou a rota:

`Casa → Amigo2 → Amigo5 → Amigo1 → Amigo4 → Amigo7 → Amigo8 → Amigo3 → Amigo6 → Casa`

O custo obtido foi **385**.

A força bruta encontrou outra rota:

`Casa → Amigo2 → Amigo5 → Amigo1 → Amigo3 → Amigo4 → Amigo7 → Amigo8 → Amigo6 → Casa`

O custo ótimo também foi **385**.

Apesar de as rotas serem diferentes, ambas possuem o mesmo custo. Portanto, o Algoritmo Genético encontrou uma solução ótima.

O Algoritmo Genético encontrou o custo ótimo pela primeira vez na **geração 46**.

### Comparação

| Método | Melhor custo | Tempo aproximado |
|---|---:|---:|
| Algoritmo Genético | **385** | **0,125 s** |
| Força Bruta | **385** | **0,034 s** |

Nesse experimento, o Algoritmo Genético conseguiu encontrar o custo ótimo confirmado pela força bruta. A força bruta apresentou um tempo menor porque o número de possibilidades ainda é relativamente pequeno.

O gráfico de convergência pode ser observado em `resultados/experimento_A.png`.

## 4. Experimento B — 15 amigos

No segundo experimento foram utilizados 15 amigos.

O Algoritmo Genético foi executado com uma população de 100 indivíduos durante 500 gerações.

A melhor rota encontrada foi:

`Casa → Amigo2 → Amigo11 → Amigo1 → Amigo10 → Amigo15 → Amigo13 → Amigo5 → Amigo3 → Amigo4 → Amigo7 → Amigo12 → Amigo8 → Amigo9 → Amigo14 → Amigo6 → Casa`

O melhor custo encontrado foi **667**.

A última melhoria registrada ocorreu na **geração 279** e o tempo de execução foi aproximadamente **0,606 segundo**.

Para 15 amigos existem:

`15! = 1.307.674.368.000`

possíveis ordens de visita.

Esse número torna a busca por força bruta inviável na prática, pois seria necessário avaliar uma quantidade extremamente grande de rotas. Por isso, neste experimento foi utilizado somente o Algoritmo Genético.

O gráfico de convergência pode ser observado em `resultados/experimento_B.png`.

## 5. Conclusão

Os experimentos mostram que o Algoritmo Genético é uma alternativa eficiente para problemas de otimização com um grande espaço de busca.

No Experimento A, com 8 amigos, foi possível comparar o resultado do AG com a força bruta. O Algoritmo Genético encontrou uma solução com custo **385**, que foi confirmado como ótimo pela força bruta. As duas abordagens encontraram rotas diferentes, mas com o mesmo custo.

No Experimento B, com 15 amigos, o número de possibilidades aumentou para mais de **1,3 trilhão de rotas**, tornando a força bruta impraticável. Nesse cenário, o Algoritmo Genético encontrou uma solução com custo **667** em aproximadamente **0,606 segundo**, com a última melhoria ocorrendo na geração **279**.

Os gráficos de convergência mostram a evolução do melhor custo ao longo das gerações, permitindo observar a melhoria das soluções durante a execução do algoritmo.