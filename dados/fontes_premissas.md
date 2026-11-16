
# Fontes de Dados e Premissas

## 1. Objetivo

Este documento tem como objetivo apresentar as fontes de dados e as premissas utilizadas na análise energética do projeto Iluminação Sustentável para Praças Comunitárias.
Como o estudo considera uma praça hipotética, serão utilizados dados de fontes confiáveis e estimativas justificadas para definir as características dos sistemas de iluminação convencional, LED e solar fotovoltaica.
Essas informações servirão como base para os cálculos de consumo de energia, custos de funcionamento e comparação das alternativas, garantindo maior transparência e coerência aos resultados apresentados no dashboard.

## 2. Fontes de Dados

[Apresentar as fontes utilizadas para obter informações sobre equipamentos, consumo energético, energia solar e custos.]

| Informação | Fonte consultada | Link ou referência | Data de acesso |
|---|---|---|---|
| Potência das luminárias | [Preencher] | [Preencher] | [Preencher] |
| Tempo de funcionamento | [Preencher] | [Preencher] | [Preencher] |
| Tarifa de energia elétrica | [Preencher] | [Preencher] | [Preencher] |
| Custos dos equipamentos | [Preencher] | [Preencher] | [Preencher] |
| Geração de energia solar | [Preencher] | [Preencher] | [Preencher] |

## 3. Premissas Adotadas

[Informar os valores e as condições consideradas para realizar os cálculos, identificando quais são estimativas e quais foram obtidos em fontes consultadas.]

### 3.1. Características da Praça

Para a realização do estudo, será considerada uma praça comunitária hipotética, localizada em uma região residencial urbana do município de Osasco, em São Paulo, e utilizada pela população para atividades de lazer e convivência.
A escolha de Osasco como município de referência foi fundamentada na disponibilidade de dados oficiais aplicáveis à análise energética e na existência de iniciativas reais de modernização da iluminação pública. Segundo a Prefeitura de Osasco (2021), o programa Cidade Iluminada já havia instalado 1.009 luminárias decorativas LED em praças, parques e áreas externas de prédios públicos até a data da publicação. Além disso, o município foi beneficiado por um projeto de eficiência energética da Enel voltado à substituição de sistemas convencionais de iluminação pública por luminárias LED.
Essas iniciativas demonstram a aplicação de tecnologias mais eficientes no município e justificam sua utilização como referência para o estudo, embora a praça analisada seja hipotética.
Como premissa inicial, a praça contará com 10 pontos de iluminação, cada um equipado com uma luminária convencional alimentada pela rede elétrica. Essa quantidade foi adotada para fins de simulação, permitindo estimar o consumo energético e comparar as alternativas propostas.
Nos três cenários analisados, será mantida a mesma quantidade de pontos de iluminação, buscando atender a necessidades equivalentes de iluminação.
A quantidade de energia elétrica consumida será estimada em kWh, considerando a potência das luminárias, a quantidade de equipamentos e o tempo de funcionamento. Os resultados serão apresentados na análise energética, com base nas premissas adotadas e nas informações técnicas consultadas.

### 3.2. Funcionamento da Iluminação

Para a análise energética, será considerado que o sistema de iluminação da praça funcionará durante o período noturno, com acionamento ao anoitecer e desligamento ao amanhecer.
De acordo com a Resolução Homologatória nº 2.590/2019 da Agência Nacional de Energia Elétrica (ANEEL), o município de Osasco possui um tempo médio diário de referência de 11 horas e 26 minutos para a estimativa do consumo de energia elétrica da iluminação pública.
Com base nesse valor, será considerado um período de 30 dias por mês, totalizando 343 horas mensais de funcionamento.
O mesmo tempo de funcionamento será adotado nos três cenários analisados, permitindo comparar o consumo energético da iluminação convencional, das luminárias LED conectadas à rede elétrica e das luminárias LED alimentadas por energia solar fotovoltaica.
O tempo utilizado representa uma referência regulatória para estimativas de faturamento, não uma medição real da praça hipotética. O funcionamento efetivo poderá variar conforme as condições locais e a época do ano.

### 3.3. Características dos Equipamentos

Para a análise energética, foram selecionados modelos reais de luminárias utilizadas em aplicações de iluminação pública, considerando potência elétrica, fluxo luminoso, eficiência energética e disponibilidade de informações técnicas verificáveis.
A escolha das tecnologias foi fundamentada também em exemplos de modernização da iluminação de praças públicas brasileiras, como a Praça Vilaboim, em São Paulo, onde luminárias convencionais de vapor de sódio e mercúrio foram substituídas por iluminação LED.

**Sistema convencional — Luminária de vapor de sódio**
Para representar o sistema convencional da praça hipotética, foi selecionada como referência a luminária REPUME, modelo DI-960 150W-VS, registrada no Inmetro sob o nº 006047/2019.
O equipamento apresenta potência nominal de 150 W, fluxo luminoso declarado de 13.485 lúmens e eficiência luminosa declarada de 89,9 lm/W.
A escolha foi fundamentada na utilização histórica de lâmpadas de vapor de sódio na iluminação pública, inclusive em praças, e na disponibilidade de características técnicas documentadas pelo Inmetro.
Para a estimativa do consumo energético do sistema convencional, também serão consideradas as perdas elétricas do reator, equipamento necessário ao funcionamento da lâmpada de vapor de sódio. Essas perdas serão fundamentadas em referências técnicas, evitando subestimar o consumo total do sistema.

**Alternativa 1 — Iluminação LED conectada à rede elétrica**
Para a primeira alternativa, foi selecionada a luminária LED REEME, modelo LD-7P-100-3000-140, registrada no Inmetro sob o nº 005531/2023.
De acordo com a entrada incluída no registro do Inmetro em 25/09/2023, o equipamento apresenta potência nominal de 100 W, fluxo luminoso declarado de 15.000 lúmens, eficiência luminosa de 150 lm/W, temperatura de cor de 3.000 K e proteção IP66.
A escolha foi fundamentada na menor potência elétrica e na maior eficiência luminosa declarada em comparação com a luminária convencional selecionada. A linha LD-7P também possui aplicação documentada em projetos de modernização da iluminação pública, como no município de Itaquaquecetuba, em São Paulo.
Durante a consulta ao Inmetro, foi identificado que o histórico do registro apresenta uma entrada excluída e outra incluída para o mesmo código de modelo, com especificações luminosas diferentes. Para a simulação, serão utilizados os dados da entrada marcada como incluída, correspondente a 15.000 lúmens e 150 lm/W.

**Alternativa 2 — Iluminação LED alimentada por energia solar fotovoltaica**
Para a segunda alternativa, será considerada a mesma luminária LED REEME de 100 W utilizada na alternativa 1, porém alimentada por um sistema fotovoltaico isolado da rede elétrica.
A proposta prevê a utilização de painéis solares, baterias para armazenamento da energia gerada e equipamentos de controle e conversão necessários para alimentar as luminárias.
A utilização do mesmo modelo LED nas duas alternativas foi escolhida para manter constantes as características do equipamento de iluminação, permitindo comparar principalmente as diferenças entre as fontes de fornecimento de energia.
As características e capacidades dos componentes fotovoltaicos serão apresentadas na seção 3.4, considerando o consumo energético previsto, as condições de geração solar de Osasco e as perdas do sistema.

**Justificativa e Limitações da Seleção**
Os equipamentos foram selecionados como referências técnicas para a simulação, com base em especificações verificáveis e na aplicação das respectivas tecnologias em sistemas de iluminação pública.
Embora os fluxos luminosos declarados sejam próximos, isso não garante que as luminárias ofereçam iluminação equivalente em toda a praça. A distribuição da luz, a altura dos postes, o espaçamento entre os pontos de iluminação e as condições de instalação também influenciam o resultado.
Assim, os modelos serão utilizados para a comparação energética inicial, sem substituir um estudo luminotécnico necessário para uma implantação real


### 3.4. Condições de Geração Solar

[Informar as premissas relacionadas à geração fotovoltaica, incluindo disponibilidade solar, perdas estimadas e armazenamento de energia, quando aplicável.]

### 3.5. Custos e Tarifas

[Registrar os valores utilizados para estimar os custos de implantação, operação e manutenção, incluindo a tarifa de energia elétrica.]

## 4. Justificativa das Premissas

[Explicar por que os valores adotados são adequados para o cenário estudado, relacionando-os às fontes disponíveis.]

## 5. Limitações dos Dados

[Identificar possíveis incertezas, ausência de medições reais e fatores que podem influenciar os resultados.]

## 6. Relação com os Cálculos Energéticos

[Explicar como os dados registrados neste documento serão utilizados nos arquivos de análise energética, comparação das alternativas e no dashboard.]
