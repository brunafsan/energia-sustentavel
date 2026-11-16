# Indicadores de Eficiência Energética e Sustentabilidade

## 1. Objetivo dos Indicadores
Os indicadores têm como objetivo avaliar e comparar o desempenho energético, econômico e ambiental das alternativas de iluminação propostas para a praça comunitária hipotética de Osasco.
Por meio de medidas quantitativas, será possível analisar o consumo de energia das luminárias, a redução da compra de eletricidade da rede, a economia financeira e o aproveitamento de energia solar renovável.
Os resultados serão apresentados no dashboard do projeto, permitindo visualizar e comparar os três cenários com base nas premissas e nos cálculos realizados.
Como o estudo considera uma praça hipotética, os indicadores representarão resultados simulados, não medições reais.

## 2. Indicadores Selecionados

### 2.1. Consumo Mensal de Energia

**Unidade:** kWh/mês

**Descrição:**
O indicador representa a quantidade de energia elétrica consumida mensalmente pelas luminárias da praça. Sua importância está em permitir a comparação do consumo entre o sistema convencional e as alternativas LED, identificando possíveis reduções no uso de energia.

**Método de cálculo:**
Consumo mensal (kWh) = (Quantidade de luminárias × Potência por luminária (W) × Horas mensais de funcionamento) ÷ 1.000
Para os três cenários, serão consideradas 10 luminárias e 343 horas de funcionamento mensal.

**Resultado estimado:**
- Sistema convencional: (10 × 168 × 343) ÷ 1.000 = 576,24 kWh/mês.
- Alternativa 1 — LED na rede: (10 × 100 × 343) ÷ 1.000 = 343 kWh/mês.
- Alternativa 2 — LED solar: (10 × 100 × 343) ÷ 1.000 = 343 kWh/mês.

Os resultados demonstram que ambas as alternativas LED apresentam menor consumo energético em relação ao sistema convencional.
Na alternativa solar, o consumo das luminárias permanece em 343 kWh/mês, pois a diferença está na fonte de fornecimento de energia, e não na potência dos equipamentos.


### 2.2. Economia Energética Estimada

**Unidade:** kWh/mês e %

**Descrição:**
O indicador representa a economia energética estimada das alternativas em relação ao sistema convencional. Serão avaliadas tanto a redução do consumo das luminárias quanto a diminuição da quantidade de eletricidade comprada da rede.
Essa distinção permite analisar os benefícios da eficiência energética das luminárias LED e do aproveitamento da energia solar fotovoltaica.

**Método de cálculo:**
- Economia absoluta (kWh/mês) = Consumo do sistema atual − Consumo da alternativa
- Economia percentual (%) = (Economia absoluta ÷ Consumo do sistema atual) × 100

Para calcular a redução da energia comprada da rede, serão utilizadas as mesmas fórmulas, substituindo o consumo pela quantidade de eletricidade adquirida da distribuidora.

**Resultado estimado:**

**Redução do consumo das luminárias:**
- Alternativa 1 — LED na rede: 576,24 − 343 = 233,24 kWh/mês (40,48%).
- Alternativa 2 — LED solar: 576,24 − 343 = 233,24 kWh/mês (40,48%).

**Redução da energia comprada da rede:**
- Alternativa 1 — LED na rede: 576,24 − 343 = 233,24 kWh/mês (40,48%).
- Alternativa 2 — LED solar: 576,24 − 0 = 576,24 kWh/mês (100%).

Na alternativa solar, a redução de 100% refere-se exclusivamente à compra de eletricidade da rede, considerando que o sistema fotovoltaico isolado atenda integralmente à demanda nas condições simuladas. As luminárias continuarão consumindo 343 kWh/mês.


### 2.3. Redução Estimada de Custos

**Unidade:** R$/mês

**Descrição:**

[Explicar como será avaliada a redução dos custos mensais de operação.]

**Método de cálculo:**

[Apresentar a fórmula utilizada para comparar os custos do sistema atual e das alternativas.]

**Resultado estimado:**

[Inserir o valor estimado da economia mensal.]

### 2.4. Participação de Energia Renovável

**Unidade:** %

**Descrição:**

[Explicar qual parcela da demanda energética será atendida pela energia solar fotovoltaica.]

**Método de cálculo:**

[Apresentar a fórmula utilizada para determinar a participação da energia renovável.]

**Resultado estimado:**

[Inserir o percentual estimado.]

## 3. Tabela Consolidada dos Indicadores

[Preencher a tabela com os resultados calculados.]

| Indicador | Sistema Atual | Alternativa 1 | Alternativa 2 |
|---|---|---|---|
| Consumo mensal (kWh) | [Valor] | [Valor] | [Valor] |
| Economia energética (%) | [Valor] | [Valor] | [Valor] |
| Redução de custos (R$/mês) | [Valor] | [Valor] | [Valor] |
| Participação renovável (%) | [Valor] | [Valor] | [Valor] |

## 4. Apresentação dos Indicadores no Dashboard

[Descrever como os indicadores serão apresentados no painel, utilizando gráficos, tabelas ou outros recursos visuais.]

## 5. Integração com os Cálculos Energéticos

[Explicar como os dados e os resultados dos cálculos realizados em Python serão utilizados para alimentar os indicadores.]

## 6. Limitações dos Indicadores

[Informar as limitações dos resultados, considerando o uso de dados estimados ou simulados e as premissas adotadas.]
