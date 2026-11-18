
# Diagrama de Funcionamento da Solução

## 1. Visão Geral do Sistema

O projeto propõe a análise de três cenários de iluminação para uma praça comunitária hipotética de Osasco: sistema convencional, iluminação LED conectada à rede elétrica e iluminação LED alimentada por energia solar fotovoltaica.
Nos dois primeiros cenários, a energia será fornecida pela rede de distribuição. Na alternativa solar, os painéis fotovoltaicos gerarão energia durante o dia, que será armazenada em baterias para alimentar as luminárias durante a noite.
O acompanhamento do desempenho energético será realizado por meio de dados estimados e simulados, sem utilização de sensores físicos. Esses dados serão processados em Python para calcular o consumo de energia, a economia estimada, os custos de operação e a participação de energia solar própria.
Os resultados serão apresentados no Neighborhood Action Dashboard, permitindo comparar os três cenários e visualizar os benefícios e as limitações de cada alternativa.

## 2. Componentes do Sistema

### 2.1. Fonte de Energia

O projeto considera duas fontes de fornecimento de energia elétrica:
- Rede elétrica: utilizada no sistema convencional e na alternativa LED conectada à rede, sendo responsável pelo fornecimento de energia durante o período noturno.
- Energia solar fotovoltaica: utilizada na segunda alternativa, por meio de 10 painéis solares de 650 W, totalizando 6,5 kWp de potência instalada. A energia gerada durante o dia será armazenada em baterias para alimentar as luminárias à noite, sem conexão com a rede elétrica.

As duas alternativas LED apresentam o mesmo consumo de iluminação, diferenciando-se principalmente pela origem da energia utilizada.


### 2.2. Equipamentos Consumidores

O projeto considera os seguintes equipamentos consumidores de energia elétrica:
- Sistema convencional: 10 luminárias de vapor de sódio de 150 W, com perdas estimadas de 18 W por reator, totalizando 168 W por ponto de iluminação.
- Alternativa 1 — LED na rede: 10 luminárias LED de 100 W, totalizando 1.000 W de potência instalada, alimentadas pela rede elétrica.
- Alternativa 2 — LED solar: as mesmas 10 luminárias LED de 100 W, alimentadas pela energia armazenada nas baterias do sistema fotovoltaico.
Na alternativa solar, também serão utilizados equipamentos de conversão e controle de energia, necessários ao funcionamento do sistema. Suas possíveis perdas energéticas serão representadas de forma simplificada pelo fator global de aproveitamento de 70% adotado nas premissas.

Os três cenários considerarão o mesmo período de funcionamento de 11 horas e 26 minutos por dia, permitindo comparar o consumo energético das luminárias.


### 2.3. Sensores ou Dados de Consumo

O projeto não utilizará sensores físicos, pois o monitoramento energético será realizado por meio de dados estimados e simulados.
Serão consideradas informações como quantidade de luminárias, potência elétrica, horas de funcionamento, período mensal de utilização e fonte de energia de cada cenário. Também serão utilizadas premissas de geração e armazenamento solar, tarifa de eletricidade e custos de manutenção para calcular os indicadores energéticos e econômicos.
Os dados serão organizados em arquivos do projeto, incluindo dados/consumo_energetico.csv, e utilizados nos cálculos em Python para estimar o consumo energético e comparar as alternativas de iluminação.
Dessa forma, o sistema permitirá avaliar os indicadores de desempenho energético sem realizar medições reais ou monitoramento em tempo real.

### 2.4. Lógica de Monitoramento

A lógica de monitoramento será baseada no processamento dos dados estimados e simulados dos três cenários de iluminação, sem utilização de sensores físicos ou medições em tempo real.
O sistema utilizará a potência, a quantidade de luminárias e o tempo de funcionamento para calcular o consumo energético mensal. Em seguida, os resultados serão comparados para identificar a economia de energia e a redução dos custos de operação em relação ao sistema convencional.
Também será considerada a quantidade de eletricidade comprada da rede, diferenciando-a do consumo total das luminárias, especialmente na alternativa solar fotovoltaica.
Com esses resultados, serão calculados os indicadores de consumo mensal, economia energética, redução de custos e participação de energia solar própria, permitindo acompanhar e comparar o desempenho estimado das alternativas no dashboard.

### 2.5. Processamento das Informações

O processamento das informações será realizado em Python, utilizando os dados estimados e simulados organizados no arquivo dados/consumo_energetico.csv.
O arquivo dashboard/calculos.py será responsável por calcular o consumo energético, a economia absoluta e percentual, os custos de operação e a participação de energia solar própria, com base nas premissas adotadas no projeto.
Os resultados serão organizados e utilizados pelo arquivo dashboard/app.py para apresentar os indicadores, gráficos e tabelas comparativas dos três cenários de iluminação.
Dessa forma, o Python permitirá transformar os dados da simulação em informações organizadas para análise e visualização no dashboard.


### 2.6. Dashboard

O Neighborhood Action Dashboard apresentará os resultados da análise energética dos três cenários de iluminação da praça comunitária, permitindo visualizar e comparar o desempenho estimado de cada alternativa.
O painel contará com quatro indicadores principais:
- Consumo energético mensal: quantidade de energia elétrica consumida pelas luminárias em cada cenário, em kWh.
- Economia de energia: redução do consumo em kWh e em percentual, em comparação com o sistema convencional.
- Redução dos custos de operação: economia mensal estimada, considerando os gastos com eletricidade e as reservas de manutenção.
- Participação de energia solar própria: percentual da demanda de iluminação atendido pela geração fotovoltaica no cenário simulado.
O dashboard também apresentará a quantidade de eletricidade comprada da rede, diferenciando-a do consumo total das luminárias.
Os resultados serão organizados em gráficos, indicadores numéricos e tabelas comparativas, facilitando a identificação das vantagens e limitações de cada alternativa. As informações serão baseadas em estimativas e simulações, não em medições em tempo real.


## 3. Diagrama de Blocos

<img width="1448" height="1086" alt="Diagrama de Iluminação Solar Bidirecional (1)" src="https://github.com/user-attachments/assets/321fc0f7-d0bb-4716-a876-f6058228a7bd" />


## 4. Descrição do Fluxo de Funcionamento

O funcionamento da solução está dividido em duas etapas: o fornecimento de energia aos sistemas de iluminação e o processamento dos dados simulados para apresentação no dashboard.

**- Fornecimento de energia:** no sistema convencional e na alternativa LED conectada à rede, a eletricidade será fornecida pela distribuidora, alimentando separadamente as luminárias de cada cenário. Na alternativa solar, os 10 painéis fotovoltaicos gerarão energia durante o dia, que será gerenciada pelo conjunto de conversão e controle e armazenada nas quatro baterias. Durante a noite, a energia armazenada será utilizada para alimentar as luminárias LED.

**- Dados simulados:** as características dos três sistemas serão representadas por dados estimados e simulados, sem utilização de sensores físicos. Os dados de consumo serão organizados em dados/consumo_energetico.csv, enquanto dados/fontes_premissas.md documentará as fontes e premissas utilizadas nos cálculos.

**- Lógica de monitoramento:** os dados serão utilizados para comparar os três cenários de iluminação, considerando o consumo energético, a eletricidade comprada da rede, a economia estimada e os custos de operação.

**- Processamento das informações:** o arquivo `dashboard/calculos.py` realizará os cálculos em Python, utilizando os dados e as premissas do projeto para determinar os indicadores energéticos e econômicos.

**- Apresentação no dashboard:** os resultados serão apresentados pelo arquivo `dashboard/app.py`, por meio de gráficos, tabelas comparativas e indicadores de consumo mensal, economia de energia, redução dos custos de operação e participação de energia solar própria.

Dessa forma, o sistema permitirá comparar o desempenho estimado das alternativas de iluminação, sem monitoramento em tempo real. Os resultados da alternativa solar estarão condicionados às premissas de geração e armazenamento adotadas na simulação.

## 5. Integração com o Neighborhood Action Dashboard

A solução energética será integrada à proposta do Neighborhood Action Dashboard, do desafio CitizenTech, por meio da apresentação de indicadores que auxiliem na análise de melhorias para espaços públicos comunitários.
Os dados estimados e simulados dos três cenários de iluminação serão processados em Python e apresentados em um painel, permitindo comparar o consumo energético, a economia de energia, os custos de operação e a participação de energia solar própria.
A visualização será realizada por meio de gráficos, tabelas comparativas e indicadores numéricos, facilitando a identificação das vantagens e limitações de cada alternativa.
Dessa forma, o dashboard funcionará como uma ferramenta de apoio à análise de soluções energéticas para a praça comunitária hipotética, contribuindo para a avaliação de alternativas mais eficientes e sustentáveis.

## 6. Limitações da Implementação

O projeto será desenvolvido como uma simulação computacional, sem instalação física dos sistemas de iluminação ou utilização de sensores reais.
As luminárias, os painéis fotovoltaicos, as baterias e os equipamentos de conversão e controle serão representados conceitualmente, com base nas características técnicas e premissas registradas em dados/fontes_premissas.md. Não serão realizados testes físicos de geração solar, armazenamento ou distribuição de energia.
A implementação em software será realizada em Python, utilizando os dados estimados e simulados organizados em dados/consumo_energetico.csv. O arquivo dashboard/calculos.py será responsável pelos cálculos de consumo energético, economia de energia, custos de operação e indicadores de desempenho dos três cenários.
Os resultados serão apresentados por meio de gráficos, tabelas e indicadores numéricos no painel desenvolvido em dashboard/app.py, sem monitoramento em tempo real ou comunicação com equipamentos físicos.
Dessa forma, a solução permitirá realizar uma comparação energética e econômica preliminar, mas não substituirá medições reais, estudos técnicos ou dimensionamentos necessários para uma eventual implantação física.

  
