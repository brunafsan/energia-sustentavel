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

[Informar quais sensores ou dados estimados/simulados serão utilizados para acompanhar o consumo energético.]

### 2.4. Lógica de Monitoramento

[Explicar como os dados serão utilizados para calcular o consumo, identificar diferenças entre as alternativas e acompanhar os indicadores.]

### 2.5. Processamento das Informações

[Descrever como o Python realizará os cálculos e organizará as informações para apresentação.]

### 2.6. Dashboard

[Explicar quais indicadores e resultados serão apresentados no painel.]

## 3. Diagrama de Blocos

[Inserir aqui o diagrama de blocos que represente as conexões entre a fonte de energia, os equipamentos consumidores, os dados de consumo, o processamento e o dashboard.]

## 4. Descrição do Fluxo de Funcionamento

[Explicar, na sequência apresentada no diagrama, como os componentes se relacionam e como os dados chegam ao dashboard.]

## 5. Integração com o Neighborhood Action Dashboard

[Explicar como a solução energética será integrada ao desafio CitizenTech, permitindo visualizar os indicadores e comparar as alternativas.]

## 6. Limitações da Implementação

[Informar quais componentes serão apenas representados conceitualmente e quais funcionalidades serão implementadas em software.]
  
