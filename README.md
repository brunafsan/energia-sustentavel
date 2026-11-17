# Iluminação Sustentável para Praças Comunitárias

## 1. Apresentação do Projeto

O projeto Iluminação Sustentável para Praças Comunitárias faz parte do desafio Neighborhood Action Dashboard — CitizenTech e tem como proposta analisar alternativas para melhorar a eficiência energética da iluminação em espaços comunitários.

O estudo considera três cenários: a utilização de luminárias convencionais, a substituição por luminárias LED conectadas à rede elétrica e a adoção de iluminação LED alimentada por energia solar fotovoltaica.

A partir dessa análise, será desenvolvido um dashboard para apresentar e comparar informações sobre consumo de energia, custos e indicadores de sustentabilidade, permitindo visualizar os possíveis benefícios de cada alternativa.

## 2. Problema Identificado

A iluminação de praças comunitárias é importante para garantir a visibilidade dos espaços durante a noite e favorecer sua utilização pela população. Entretanto, sistemas de iluminação com equipamentos pouco eficientes podem apresentar um consumo elevado de energia elétrica, aumentando os custos de manutenção desses espaços.

Além disso, a dependência exclusiva da rede elétrica limita o aproveitamento de fontes renováveis, como a energia solar. Diante desse cenário, surge a necessidade de avaliar alternativas que permitam manter uma iluminação adequada, reduzir o consumo de energia e contribuir para a sustentabilidade dos espaços públicos.

## 3. Objetivo

O objetivo do projeto é analisar a viabilidade de alternativas mais eficientes e sustentáveis para a iluminação de praças comunitárias, considerando o consumo de energia elétrica, os custos envolvidos e os possíveis benefícios ambientais.

Para isso, serão realizados cálculos e estimativas energéticas de três cenários de iluminação, permitindo comparar seus resultados. As informações obtidas serão organizadas em um dashboard, que apresentará indicadores para facilitar a visualização das diferenças entre as alternativas e apoiar a identificação da solução mais adequada ao espaço estudado.

## 4. Solução Proposta

A solução proposta consiste em analisar alternativas para melhorar a eficiência energética da iluminação de praças comunitárias, considerando três cenários: o sistema convencional, a utilização de luminárias LED alimentadas pela rede elétrica e a adoção de luminárias LED com energia solar fotovoltaica.

A comparação será realizada por meio de estimativas de consumo energético, custos, viabilidade técnica e impactos ambientais, buscando identificar os benefícios e as limitações de cada alternativa.

Para complementar a análise, será desenvolvido um dashboard em Python, utilizando dados estimados ou simulados para apresentar indicadores de consumo, economia energética e sustentabilidade. Dessa forma, será possível visualizar os resultados e apoiar a avaliação das soluções propostas.

## 5. Cenários Analisados

### 5.1. Sistema Atual

O cenário atual representa uma praça comunitária com iluminação convencional, alimentada exclusivamente pela rede elétrica. Esse sistema será utilizado como referência para estimar o consumo de energia e os custos mensais de funcionamento.

A partir desses resultados, será possível comparar o desempenho das alternativas propostas e identificar oportunidades de melhoria na eficiência energética.

### 5.2. Alternativa 1 — Iluminação LED

A primeira alternativa consiste na substituição das luminárias convencionais por luminárias LED, mantendo o fornecimento de energia pela rede elétrica.

A tecnologia LED apresenta maior eficiência energética, permitindo reduzir o consumo de eletricidade em comparação com equipamentos convencionais de desempenho equivalente. A análise considerará a economia estimada, os custos de implantação e as condições necessárias para realizar a substituição.

### 5.3. Alternativa 2 — Iluminação Solar Fotovoltaica

A segunda alternativa propõe a utilização de luminárias LED alimentadas por energia solar fotovoltaica. Nesse sistema, a energia solar é convertida em eletricidade por painéis fotovoltaicos, podendo ser armazenada em baterias para utilização durante a noite.

A análise considerará a capacidade estimada de geração de energia, a redução da dependência da rede elétrica, os custos de implantação e manutenção e as condições técnicas necessárias para o funcionamento do sistema.

## 6. Análise Energética

A análise energética foi realizada considerando uma praça comunitária hipotética localizada em Osasco, São Paulo, com 10 pontos de iluminação e funcionamento de 11 horas e 26 minutos por dia, equivalente a 343 horas mensais.

Foram comparados três cenários: iluminação convencional de vapor de sódio, iluminação LED conectada à rede elétrica e iluminação LED alimentada por energia solar fotovoltaica.

O sistema convencional apresenta consumo estimado de 576,24 kWh mensais, enquanto as duas alternativas LED apresentam demanda de 343,00 kWh por mês. A substituição das luminárias convencionais por LED representa uma redução estimada de 233,24 kWh mensais, equivalente a aproximadamente 40,48%.

Na alternativa solar fotovoltaica, foi considerado um sistema de 6,5 kWp, com geração útil estimada de 13,51 kWh por dia e armazenamento em baterias. Nas condições simuladas, a geração estimada é superior à demanda diária das luminárias LED, de aproximadamente 11,43 kWh.

Os resultados são baseados em dados técnicos e premissas adotadas pela equipe, não correspondendo a medições realizadas em uma instalação real.

Os dados utilizados, as fórmulas e os cálculos detalhados estão disponíveis no arquivo `docs/analise_energetica.md`.

## 7. Indicadores de Sustentabilidade

O projeto compara três alternativas de iluminação para a praça comunitária, considerando o consumo de energia elétrica, os custos estimados e a utilização de fontes renováveis.

| Critério | Convencional | LED conectado à rede | LED solar fotovoltaico |
|---|---|---|---|
| Consumo mensal das luminárias | 576,24 kWh | 343,00 kWh | 343,00 kWh |
| Energia utilizada | Rede elétrica | Rede elétrica | Solar fotovoltaica |
| Custo mensal de eletricidade | R$ 250,18 | R$ 148,92 | R$ 0,00* |
| Investimento inicial estimado | R$ 0,00 | R$ 12.500,00 | R$ 63.030,00 |
| Reserva mensal de manutenção | R$ 30,00 | R$ 20,00 | R$ 120,00 |

*O custo de eletricidade da alternativa solar considera que o sistema fotovoltaico isolado consiga atender integralmente à demanda nas condições simuladas. Esse valor não representa ausência de consumo energético ou de despesas operacionais.*

A iluminação convencional apresenta o maior consumo de energia elétrica entre os cenários analisados. A alternativa LED conectada à rede reduz a demanda energética em aproximadamente 40,48%, mantendo o fornecimento pela distribuidora.

A alternativa solar apresenta o mesmo consumo das luminárias LED, mas utiliza geração fotovoltaica e armazenamento em baterias para reduzir a dependência da rede elétrica. Entretanto, exige um investimento inicial significativamente maior e apresenta custos adicionais relacionados à manutenção dos componentes.

Dessa forma, a comparação permite avaliar os benefícios e as limitações de cada alternativa, considerando que a redução do consumo de eletricidade da rede não garante, isoladamente, maior viabilidade econômica.

A análise detalhada das alternativas será apresentada no arquivo `docs/comparacao_alternativas.md`.


## 8. Dashboard

[Explicar o funcionamento do dashboard e quais informações serão apresentadas.]
O projeto utiliza indicadores energéticos, econômicos e de sustentabilidade para avaliar os três cenários de iluminação da praça comunitária.

Os principais indicadores considerados são:

1. **Consumo mensal de energia (kWh):** representa a quantidade de energia necessária para o funcionamento das luminárias. O sistema convencional apresenta consumo estimado de 576,24 kWh por mês, enquanto as alternativas LED apresentam 343,00 kWh.

2. **Economia de energia (%):** indica a redução do consumo em relação ao sistema convencional. A substituição por luminárias LED proporciona uma economia estimada de 40,48%.

3. **Custo mensal de eletricidade (R$):** apresenta os gastos estimados com a energia adquirida da rede elétrica. Os valores são de R$ 250,18 para o sistema convencional, R$ 148,92 para o LED conectado à rede e R$ 0,00 para o sistema solar, desde que a geração e o armazenamento atendam à demanda nas condições simuladas.

4. **Participação de energia renovável (%):** representa a proporção da demanda energética atendida pela geração solar. Na alternativa fotovoltaica, a participação estimada é de 100% nas condições adotadas, enquanto os outros cenários não possuem geração renovável própria considerada no projeto.

5. **Custo operacional mensal (R$):** considera os gastos estimados com eletricidade e a reserva mensal de manutenção. Os valores são de R$ 280,18 para o sistema convencional, R$ 168,92 para o LED conectado à rede e R$ 120,00 para o sistema solar nas condições simuladas.

Esses indicadores permitem visualizar as diferenças entre as alternativas e avaliar os benefícios energéticos, econômicos e ambientais esperados.

Os resultados serão apresentados no dashboard desenvolvido em Python, utilizando os dados do arquivo `dados/consumo_energetico.csv` e as funções implementadas em `dashboard/calculos.py`.

A descrição detalhada dos indicadores está disponível no arquivo `docs/indicadores.md`.

## 9. Tecnologias Utilizadas

O projeto utiliza a linguagem Python para o desenvolvimento dos cálculos energéticos e do dashboard, responsável pela apresentação dos indicadores e pela comparação das alternativas de iluminação.

O GitHub é utilizado para armazenar e organizar os arquivos do projeto, incluindo a documentação técnica, os dados e os códigos desenvolvidos. Os documentos são estruturados em Markdown (.md), enquanto os dados de consumo energético são organizados em formato CSV (.csv), permitindo sua utilização nos cálculos realizados em Python.

## 10. Estrutura do Repositório

O repositório foi organizado em três pastas principais: `dados`, `docs` e `dashboard`, além do arquivo `README.md`, que apresenta as informações gerais do projeto.

- **dados:** contém o arquivo `consumo_energetico.csv`, destinado ao armazenamento dos dados utilizados nos cálculos, e o documento `fontes_premissas.md`, responsável pelo registro das fontes consultadas e das premissas adotadas.

- **docs:** reúne a documentação técnica do projeto, incluindo o diagnóstico do problema, a análise energética, a comparação das alternativas, o diagrama da solução, os indicadores de sustentabilidade e as referências e limitações.

- **dashboard:** contém os arquivos Python responsáveis pelos cálculos e pela apresentação dos resultados. O arquivo `calculos.py` reúne as funções de cálculo energético, enquanto `app.py` corresponde ao programa principal do dashboard.

- **README.md:** apresenta a proposta, os objetivos, as alternativas analisadas e as orientações gerais para compreender e executar o projeto.

## 11. Como Executar o Projeto

O dashboard foi desenvolvido em Python e funciona por meio do terminal, sem necessidade de instalar bibliotecas externas.

Para executar o projeto:

1. Baixe o repositório pelo GitHub, utilizando a opção **Code → Download ZIP**.
2. Extraia o arquivo ZIP no computador.
3. Abra a pasta principal do projeto no Visual Studio Code.
4. Abra o terminal integrado do VS Code.
5. Execute o seguinte comando:

   `python dashboard/app.py`

O programa carrega os dados do arquivo `dados/consumo_energetico.csv`, utiliza as funções de `dashboard/calculos.py` e apresenta os resultados dos três cenários de iluminação.

A saída inclui o consumo energético, a comparação dos custos, os indicadores de sustentabilidade e os benefícios estimados.

**Requisito:** ter o Python 3 instalado no computador.

## 12. Resultados Esperados

Espera-se que o projeto permita identificar alternativas de iluminação mais eficientes e sustentáveis para praças comunitárias, considerando o consumo energético, os custos e os impactos ambientais de cada solução.

A utilização de luminárias LED poderá contribuir para a redução do consumo de eletricidade, enquanto a alternativa com energia solar fotovoltaica poderá diminuir a dependência da rede elétrica e ampliar o aproveitamento de fontes renováveis.

Além disso, espera-se que o dashboard facilite a visualização e a comparação dos indicadores energéticos, auxiliando na avaliação das alternativas e na tomada de decisões relacionadas à melhoria da infraestrutura comunitária.

Os benefícios efetivos de cada solução serão avaliados a partir dos cálculos e das estimativas desenvolvidos ao longo do projeto.

## 13. Limitações

O projeto apresenta uma simulação de alternativas de iluminação sustentável para uma praça comunitária hipotética, utilizando dados técnicos e estimativas de consumo, geração de energia e custos.

As principais limitações consideradas são:

- **Dados simulados:** os resultados não foram obtidos por medições em uma praça real.
- **Condições climáticas:** a geração solar pode variar conforme a época do ano, a nebulosidade e as condições de instalação.
- **Armazenamento de energia:** a capacidade estimada das baterias não garante o funcionamento contínuo durante vários dias de baixa geração solar.
- **Custos estimados:** os investimentos e as despesas de manutenção são premissas do projeto e podem diferir dos valores reais de instalação e operação.
- **Iluminação da praça:** não foi realizado um estudo luminotécnico para confirmar se as alternativas oferecem níveis equivalentes de iluminação.
- **Manutenção e vida útil:** não foram simuladas todas as substituições futuras de equipamentos, especialmente das baterias do sistema fotovoltaico.

Portanto, os resultados permitem comparar os cenários nas condições estabelecidas, mas não substituem um projeto técnico detalhado para implantação real.

As referências e limitações adicionais estão documentadas em `docs/referencias_limitacoes.md`.


## 14. Referências

As informações utilizadas no projeto foram baseadas em referências técnicas sobre iluminação pública, consumo de energia elétrica, sistemas fotovoltaicos e armazenamento em baterias.

Foram consideradas informações de órgãos reguladores, fabricantes de equipamentos e fontes relacionadas à geração de energia solar, incluindo dados da Agência Nacional de Energia Elétrica (ANEEL).

As referências utilizadas para definir a potência das luminárias, o tempo de funcionamento, a tarifa de energia, a geração fotovoltaica e os custos estimados estão organizadas nos seguintes arquivos:

- `dados/fontes_premissas.md` — fontes dos dados e justificativas das premissas adotadas.
- `docs/referencias_limitacoes.md` — referências técnicas e limitações da análise.

Os resultados apresentados são estimativas baseadas nessas premissas e não representam medições realizadas em uma instalação real.
