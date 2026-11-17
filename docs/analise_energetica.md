# Análise do Consumo Energético

## 1. Caracterização do Sistema de Iluminação

O projeto considera uma praça comunitária hipotética localizada no município de Osasco, em São Paulo, com 10 pontos de iluminação destinados ao uso noturno do espaço público.

O sistema inicial é composto por luminárias convencionais de vapor de sódio de 150 W, com acréscimo estimado de 18 W referentes às perdas do reator, totalizando 168 W por ponto de iluminação.

Para avaliar possibilidades de melhoria, serão analisadas duas alternativas: a substituição das luminárias convencionais por modelos LED de 100 W conectados à rede elétrica e a utilização das mesmas luminárias LED alimentadas por um sistema de energia solar fotovoltaica com armazenamento em baterias.

Nos três cenários, será considerado um funcionamento diário de 11 horas e 26 minutos, equivalente a 343 horas mensais, adotando um período de 30 dias. A quantidade de luminárias e o tempo de funcionamento serão mantidos para permitir a comparação do consumo energético entre as alternativas.

## 2. Dados Utilizados

| Equipamento | Quantidade | Potência (W) | Horas de uso por dia |
|---|---:|---:|---:|
| Luminária convencional de vapor de sódio (com reator) | 10 | 168 | 11,43 |
| Luminária LED conectada à rede elétrica | 10 | 100 | 11,43 |
| Luminária LED alimentada por energia solar | 10 | 100 | 11,43 |

## 3. Premissas Adotadas

A análise energética será realizada com base em uma praça comunitária hipotética localizada em Osasco, São Paulo. Para a simulação, foram considerados 10 pontos de iluminação, mantendo a mesma quantidade de luminárias nos três cenários analisados.

O tempo de funcionamento adotado será de 11 horas e 26 minutos por dia, equivalente a 343 horas mensais, considerando meses padronizados de 30 dias. Esse período foi definido com base na referência da Agência Nacional de Energia Elétrica (ANEEL) para a estimativa do consumo da iluminação pública no município de Osasco.

As potências das luminárias foram estabelecidas a partir de modelos reais registrados no Inmetro. No sistema convencional, será considerada uma lâmpada de vapor de sódio de 150 W, acrescida de 18 W de perdas estimadas do reator, totalizando 168 W por ponto de iluminação. Nas alternativas LED conectada à rede elétrica e solar fotovoltaica, serão utilizadas luminárias de 100 W.

Os valores representam condições de referência para a simulação, não medições realizadas em uma praça existente. As fontes consultadas, as justificativas das escolhas e as limitações dos dados estão detalhadas no arquivo `dados/fontes_premissas.md`.

## 4. Cálculo do Consumo Energético

O consumo energético será calculado considerando a potência elétrica de cada luminária, a quantidade de equipamentos e o tempo de funcionamento.

A fórmula utilizada será:

**E = (P × Q × t) / 1000**

Onde:

- **E:** energia elétrica consumida (kWh).
- **P:** potência elétrica de cada luminária (W).
- **Q:** quantidade de luminárias.
- **t:** tempo de funcionamento (h).

A divisão por 1000 é necessária para converter o resultado de Wh (watt-hora) para kWh (quilowatt-hora).

Para os cálculos diários, será considerado um período de 11 horas e 26 minutos, equivalente a aproximadamente 11,4333 horas. Para os cálculos mensais, serão utilizadas 343 horas, correspondentes a 30 dias de funcionamento.

A mesma fórmula será aplicada aos três cenários, permitindo comparar a energia consumida pelas luminárias convencionais e LED. No cenário solar fotovoltaico, o consumo das luminárias será calculado separadamente da energia gerada pelo sistema solar.

### 4.2. Consumo Diário

O consumo diário foi estimado considerando 10 luminárias em funcionamento durante 11 horas e 26 minutos por dia, equivalentes a aproximadamente 11,4333 horas.

**Cenário 1 — Iluminação convencional**

O sistema convencional utiliza 10 luminárias de vapor de sódio, com potência total estimada de 168 W por ponto, incluindo as perdas do reator.

E = (168 × 10 × 11,4333) / 1000

**Consumo diário: 19,21 kWh**

**Cenário 2 — Iluminação LED conectada à rede elétrica**

A primeira alternativa utiliza 10 luminárias LED de 100 W, alimentadas pela rede elétrica.

E = (100 × 10 × 11,4333) / 1000

**Consumo diário: 11,43 kWh**

**Cenário 3 — Iluminação LED alimentada por energia solar fotovoltaica**

A segunda alternativa utiliza as mesmas 10 luminárias LED de 100 W, porém alimentadas por um sistema fotovoltaico com armazenamento em baterias.

E = (100 × 10 × 11,4333) / 1000

**Consumo diário: 11,43 kWh**

O consumo energético das luminárias LED é igual nos cenários 2 e 3, pois a potência e o tempo de funcionamento são os mesmos. A diferença está na origem da eletricidade: enquanto o cenário 2 utiliza energia da rede elétrica, o cenário 3 prevê o fornecimento por geração solar fotovoltaica.

Os valores apresentados representam a demanda energética diária das luminárias, sem incluir eventuais consumos auxiliares dos equipamentos de conversão e controle.


### 4.3. Consumo Mensal

O consumo energético mensal foi calculado considerando o funcionamento das 10 luminárias durante 343 horas por mês, conforme as premissas adotadas para a simulação.

**Cenário 1 — Iluminação convencional**

O sistema convencional possui 10 luminárias com potência estimada de 168 W por ponto, incluindo as perdas do reator.

E = (168 × 10 × 343) / 1000

**Consumo mensal: 576,24 kWh**

**Cenário 2 — Iluminação LED conectada à rede elétrica**

A primeira alternativa utiliza 10 luminárias LED de 100 W alimentadas pela rede elétrica.

E = (100 × 10 × 343) / 1000

**Consumo mensal: 343,00 kWh**

**Cenário 3 — Iluminação LED alimentada por energia solar fotovoltaica**

A segunda alternativa utiliza 10 luminárias LED de 100 W, alimentadas por um sistema fotovoltaico com armazenamento em baterias.

E = (100 × 10 × 343) / 1000

**Consumo mensal: 343,00 kWh**

Os resultados mostram que a substituição das luminárias convencionais por modelos LED reduz a demanda energética mensal de 576,24 kWh para 343,00 kWh, representando uma economia estimada de 233,24 kWh por mês, equivalente a aproximadamente 40,48%.

Na alternativa solar fotovoltaica, a demanda energética das luminárias permanece em 343,00 kWh mensais. Entretanto, a proposta prevê que essa energia seja fornecida pelo sistema solar, reduzindo a necessidade de compra de eletricidade da rede nas condições simuladas.

Os valores representam estimativas baseadas em um mês padronizado de 30 dias e não correspondem a medições reais.


## 5. Consumo Energético Total

O consumo energético total foi estimado considerando os 10 pontos de iluminação da praça comunitária hipotética e o funcionamento mensal de 343 horas.

A tabela apresenta os resultados obtidos para cada cenário analisado.

| Cenário | Potência total (W) | Consumo diário (kWh) | Consumo mensal (kWh) |
|---|---:|---:|---:|
| Iluminação convencional | 1.680 | 19,21 | 576,24 |
| Iluminação LED conectada à rede | 1.000 | 11,43 | 343,00 |
| Iluminação LED solar fotovoltaica | 1.000 | 11,43 | 343,00 |

O sistema convencional apresenta o maior consumo energético, com 576,24 kWh mensais. As duas alternativas LED apresentam uma demanda de 343,00 kWh por mês, representando uma redução estimada de 233,24 kWh em relação ao sistema convencional.

Na alternativa solar fotovoltaica, a demanda das luminárias permanece igual à do sistema LED conectado à rede elétrica. Entretanto, o fornecimento de energia é previsto por meio de painéis solares e baterias, permitindo reduzir a dependência da distribuidora.

Os resultados correspondem a cenários alternativos para a mesma praça e não devem ser somados, pois representam diferentes possibilidades de iluminação para os mesmos 10 pontos.


## 6. Análise dos Resultados

A análise dos resultados demonstra que a substituição das luminárias convencionais por modelos LED pode contribuir para a redução do consumo energético da praça comunitária.

O sistema convencional apresenta consumo estimado de 576,24 kWh mensais, enquanto as alternativas LED apresentam demanda de 343,00 kWh por mês. Essa diferença representa uma redução de 233,24 kWh mensais, equivalente a aproximadamente 40,48% em relação ao sistema convencional.

Embora as alternativas LED conectada à rede elétrica e solar fotovoltaica apresentem o mesmo consumo energético, elas diferem na origem da eletricidade utilizada. A primeira depende do fornecimento da distribuidora, enquanto a segunda prevê a utilização de painéis solares e baterias para atender à demanda noturna.

Na alternativa fotovoltaica, o sistema proposto possui potência instalada de 6,5 kWp e geração útil estimada de 13,51 kWh por dia, considerando as condições de irradiação e as perdas adotadas na simulação. Esse valor é superior à demanda diária de aproximadamente 11,43 kWh das luminárias, indicando a possibilidade de atendimento energético nas condições consideradas. Entretanto, a geração poderá variar conforme as condições meteorológicas e as características da instalação.

Os resultados obtidos serão utilizados na comparação das alternativas, considerando também os investimentos iniciais, os custos de funcionamento e as limitações de cada sistema.

Além disso, os dados servirão como base para os indicadores apresentados no dashboard, permitindo visualizar o consumo energético, a economia estimada e as diferenças entre as soluções analisadas.

Como o estudo utiliza uma praça hipotética e valores de referência, os resultados representam estimativas para avaliação das alternativas, não garantindo o mesmo desempenho em uma instalação real.
