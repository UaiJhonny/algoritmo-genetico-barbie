# Algoritmo Genético - Problema da Barbie

## Objetivo

Este projeto implementa um Algoritmo Genético para resolver o Problema da Barbie.

O objetivo é encontrar a melhor ordem para que a Barbie visite seus amigos e depois retorne para casa, buscando minimizar o custo total do percurso.

O custo entre dois pontos é calculado utilizando o algoritmo A*, considerando os diferentes tipos de terreno presentes no mapa.

Para evitar a execução repetida do A*, os custos entre todos os pontos são calculados previamente e armazenados em uma matriz de custos. Durante a execução do Algoritmo Genético, somente essa matriz é utilizada para avaliar as rotas.

A semente utilizada nos experimentos foi baseada na matrícula:

```text
2024105231940012
Representação da solução

Cada solução é representada por um cromossomo, que corresponde a uma permutação dos amigos que a Barbie deve visitar.

Por exemplo, para 8 amigos:

[Amigo4, Amigo2, Amigo6, Amigo3, Amigo1, Amigo8, Amigo7, Amigo5]

Cada amigo aparece exatamente uma vez no cromossomo.

A rota completa considera a saída da casa da Barbie, a visita aos amigos na ordem definida pelo cromossomo e o retorno para casa.

Algoritmo A* e matriz de custos

O algoritmo A* foi reutilizado do trabalho anterior para calcular o menor custo de deslocamento entre dois pontos do mapa.

O mapa possui diferentes tipos de terreno, cada um com um custo diferente:

Terreno	Custo
Grama (G)	5
Asfalto (A)	1
Terra (T)	3
Paralelepípedo (P)	10
Edifício (E)	Bloqueado

Os edifícios não podem ser atravessados pela Barbie.

Antes da execução do Algoritmo Genético, o A* é executado para calcular o custo do menor caminho entre todos os pontos importantes: a casa da Barbie e os amigos.

Esses valores são armazenados em uma matriz de custos.

A matriz possui dimensão (N+1) × (N+1), considerando os N amigos e a casa da Barbie.

Por exemplo, para 8 amigos:

Casa + 8 amigos = 9 pontos

Durante a execução do Algoritmo Genético, o A* não é executado novamente. O custo das rotas é obtido diretamente da matriz previamente calculada.

Funcionamento do Algoritmo Genético

O Algoritmo Genético trabalha com uma população de possíveis soluções e busca melhorar essas soluções ao longo das gerações.

O processo utilizado neste projeto é:

Gerar uma população inicial de rotas aleatórias.
Calcular o custo e o fitness de cada rota.
Selecionar indivíduos utilizando seleção por roleta.
Aplicar o crossover Order Crossover (OX) para gerar novos indivíduos.
Aplicar mutação por troca de posições (swap).
Manter os melhores indivíduos da geração utilizando elitismo.
Formar uma nova população.
Repetir o processo durante o número definido de gerações.
Armazenar a melhor solução encontrada durante toda a execução.
Parâmetros utilizados
Parâmetro	Experimento A	Experimento B
Número de amigos	8	15
Tamanho da população	50	100
Número de gerações	300	500
Taxa de crossover	80%	80%
Taxa de mutação	3%	3%
Elitismo	2 indivíduos	2 indivíduos

A população inicial é formada por permutações aleatórias dos amigos, garantindo que cada amigo apareça uma única vez em cada cromossomo.

A melhor solução encontrada é mantida ao longo das gerações para evitar que uma solução de melhor qualidade seja perdida durante a evolução da população.

Operadores genéticos
Seleção por roleta

A seleção dos indivíduos é realizada pelo método da roleta.

Cada indivíduo recebe uma probabilidade de seleção proporcional ao seu fitness. Dessa forma, soluções com maior fitness possuem maior chance de serem escolhidas como pais, mas indivíduos com fitness menor também podem ser selecionados.

O fitness utilizado é:

fitness = 1 / (1 + custo)

Quanto menor o custo da rota, maior será o fitness do indivíduo.

Crossover Order Crossover (OX)

O crossover utilizado é o Order Crossover (OX), adequado para problemas em que o cromossomo representa uma permutação.

Dois pontos são escolhidos no primeiro pai e o trecho entre eles é copiado para o filho. Em seguida, os genes do segundo pai que ainda não estão presentes são inseridos na ordem em que aparecem.

Esse procedimento mantém a validade da permutação, evitando que um amigo apareça mais de uma vez no mesmo cromossomo.

A taxa de crossover utilizada nos experimentos foi de 80%.

Mutação por troca (Swap)

A mutação utilizada é a mutação por troca de posições.

Duas posições aleatórias do cromossomo são escolhidas e seus valores são trocados.

Por exemplo:

Antes:

[Amigo1, Amigo2, Amigo3, Amigo4]

Depois:

[Amigo1, Amigo4, Amigo3, Amigo2]

A taxa de mutação utilizada foi de 3% por cromossomo.

Elitismo

O elitismo mantém os melhores indivíduos da população atual na próxima geração.

Neste projeto, os 2 melhores indivíduos são preservados a cada geração.

Isso ajuda a garantir que uma boa solução encontrada pelo Algoritmo Genético não seja perdida durante os processos de seleção, crossover e mutação.

Geração das posições dos amigos

As posições dos amigos são geradas aleatoriamente a partir das posições válidas do mapa.

Somente posições que não correspondem a edifícios são consideradas válidas. As posições são escolhidas sem repetição, garantindo que dois amigos não ocupem a mesma posição.

Para garantir que os experimentos possam ser reproduzidos, é utilizado um seed fixo no gerador de números aleatórios.

Neste projeto foi utilizado:

Seed = 2024105231940012
Experimento A — 8 amigos

O primeiro experimento utiliza 8 amigos.

Nesse caso, é possível comparar o resultado obtido pelo Algoritmo Genético com uma solução ótima encontrada por força bruta.

Como existem 8 amigos, o número de possíveis ordens de visita é:

8! = 40.320 rotas
Posições geradas

As posições utilizadas no experimento foram:

Amigo	Posição
Amigo1	(3, 18)
Amigo2	(21, 14)
Amigo3	(23, 35)
Amigo4	(19, 40)
Amigo5	(12, 21)
Amigo6	(25, 26)
Amigo7	(19, 41)
Amigo8	(39, 27)
Resultado do Algoritmo Genético

A melhor rota encontrada pelo Algoritmo Genético foi:

Casa → Amigo2 → Amigo5 → Amigo1 → Amigo4 → Amigo7 → Amigo8 → Amigo3 → Amigo6 → Casa

O melhor custo encontrado foi:

385

O Algoritmo Genético encontrou esse custo pela primeira vez na:

Geração 46

O tempo de execução foi aproximadamente:

0,125 segundos
Resultado da força bruta

A força bruta encontrou outra ordem de visita, mas com o mesmo custo:

Casa → Amigo2 → Amigo5 → Amigo1 → Amigo3 → Amigo4 → Amigo7 → Amigo8 → Amigo6 → Casa

O custo ótimo confirmado pela força bruta foi:

385

O tempo de execução da força bruta foi aproximadamente:

0,034 segundos
Comparação

O Algoritmo Genético encontrou o mesmo custo obtido pela força bruta.

Portanto:

AG encontrou o ótimo: Sim
Custo do AG: 385
Custo ótimo: 385

Isso demonstra que, neste experimento, o Algoritmo Genético foi capaz de encontrar a solução ótima.

Experimento B — 15 amigos

O segundo experimento utiliza 15 amigos.

Nesse caso, a quantidade de possíveis rotas cresce de forma muito grande.

O número de permutações possíveis é:

15! = 1.307.674.368.000 rotas

Esse número corresponde a mais de 1,3 trilhão de possíveis ordens de visita.

Posições geradas

As posições utilizadas no experimento foram:

Amigo	Posição
Amigo1	(3, 18)
Amigo2	(21, 14)
Amigo3	(23, 35)
Amigo4	(19, 40)
Amigo5	(12, 21)
Amigo6	(25, 26)
Amigo7	(19, 41)
Amigo8	(39, 27)
Amigo9	(40, 6)
Amigo10	(9, 27)
Amigo11	(0, 5)
Amigo12	(36, 39)
Amigo13	(12, 33)
Amigo14	(31, 32)
Amigo15	(3, 35)
Resultado

A melhor rota encontrada pelo Algoritmo Genético foi:

Casa → Amigo2 → Amigo11 → Amigo1 → Amigo10 → Amigo15 → Amigo13 → Amigo5 → Amigo3 → Amigo4 → Amigo7 → Amigo12 → Amigo8 → Amigo9 → Amigo14 → Amigo6 → Casa

O melhor custo encontrado foi:

667

A última melhoria da melhor solução ocorreu na:

Geração 279

O tempo de execução foi aproximadamente:

0,606 segundos

Não foi executada a força bruta neste experimento devido à quantidade extremamente grande de rotas possíveis.

Estrutura do projeto

O projeto está organizado da seguinte forma:

algoritmo-genetico-barbie/
│
├── README.md
├── relatorio.md
│
├── resultados/
│   ├── experimento_A.png
│   └── experimento_B.png
│
└── src/
    ├── algoritmo_genetico.py
    ├── astar.py
    ├── avaliacao.py
    ├── crossover.py
    ├── elitismo.py
    ├── experimento_A.py
    ├── experimento_B.py
    ├── forca_bruta.py
    ├── gerar_amigos.py
    ├── gerar_graficos.py
    ├── main.py
    ├── mapa.py
    ├── matriz_custos.py
    ├── mutacao.py
    ├── populacao.py
    ├── selecao.py
    │
    ├── teste_algoritmo_genetico.py
    ├── teste_astar.py
    ├── teste_avaliacao.py
    ├── teste_crossover.py
    ├── teste_elitismo.py
    ├── teste_forca_bruta.py
    ├── teste_gerar_amigos.py
    ├── teste_matriz.py
    ├── teste_mutacao.py
    ├── teste_populacao.py
    └── teste_selecao.py
Como executar o projeto

O projeto foi desenvolvido em Python.

Executar o programa principal

A partir da pasta raiz do projeto, execute:

python src/main.py
Executar o Experimento A
python src/experimento_A.py
Executar o Experimento B
python src/experimento_B.py
Gerar os gráficos
python src/gerar_graficos.py

Os gráficos são armazenados na pasta resultados/.

Comparação dos experimentos

Os dois experimentos permitem observar o comportamento do Algoritmo Genético em problemas com diferentes tamanhos de espaço de busca.

Característica	Experimento A	Experimento B
Número de amigos	8	15
Possibilidades	40.320	1.307.674.368.000
População	50	100
Gerações	300	500
Melhor custo encontrado	385	667
Comparação com força bruta	Sim	Não
Força bruta viável	Sim	Não

No Experimento A, como existem apenas 40.320 possibilidades, foi possível utilizar força bruta para encontrar a solução ótima e comparar diretamente com o Algoritmo Genético.

O Algoritmo Genético encontrou o mesmo custo da solução ótima, igual a 385, sendo que essa solução foi encontrada pela primeira vez na geração 46.

No Experimento B, o número de possibilidades aumenta para aproximadamente 1,3 trilhão. Dessa forma, testar todas as rotas por força bruta seria inviável.

O Algoritmo Genético foi utilizado como uma alternativa para buscar uma boa solução sem precisar avaliar todas as possibilidades.

Nesse experimento, o algoritmo encontrou uma solução com custo 667, sendo registrada uma última melhoria na geração 279.

Os resultados mostram que o aumento do número de amigos aumenta significativamente o espaço de busca. O Algoritmo Genético permite trabalhar com esse espaço de busca utilizando uma população limitada e evoluindo as soluções ao longo das gerações.

Gráficos

Os gráficos de convergência dos experimentos são armazenados na pasta resultados/.

Experimento A

O gráfico mostra a evolução do melhor custo encontrado ao longo das gerações para o caso com 8 amigos.

Experimento B

O gráfico mostra a evolução do melhor custo encontrado ao longo das gerações para o caso com 15 amigos.

Conclusão

O projeto apresentou a aplicação de um Algoritmo Genético para resolver o problema de definição da ordem de visita dos amigos da Barbie, considerando o custo real dos caminhos no mapa.

O algoritmo A* foi utilizado previamente para calcular os menores custos entre a casa da Barbie e os amigos, além dos custos entre os próprios amigos. Esses valores foram armazenados em uma matriz de custos e reutilizados durante a execução do Algoritmo Genético.

No Experimento A, com 8 amigos, foi possível comparar o Algoritmo Genético com a força bruta. O Algoritmo Genético encontrou a solução ótima, com custo 385, igual ao resultado obtido pela força bruta.

No Experimento B, com 15 amigos, o número de possibilidades chegou a 1.307.674.368.000 rotas, tornando a força bruta inviável. Nesse cenário, o Algoritmo Genético encontrou uma solução com custo 667 em aproximadamente 0,606 segundo.

Assim, os experimentos demonstram como o Algoritmo Genético pode ser utilizado para encontrar boas soluções em problemas de otimização combinatória com um grande espaço de busca, sem a necessidade de testar todas as possibilidades.