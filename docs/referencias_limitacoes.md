# Referências e Limitações do Projeto

## 1. Referências

O projeto Iluminação Sustentável para Praças Comunitárias foi desenvolvido com base em referências técnicas sobre iluminação pública, eficiência energética, energia solar fotovoltaica e custos de implantação.

Foram consultados registros do Inmetro, documentos da ANEEL, estudos sobre disponibilidade solar, informações de órgãos públicos e preços comerciais de equipamentos.

Além dessas fontes, foram adotadas premissas para simular o funcionamento de uma praça comunitária hipotética em Osasco, São Paulo. As informações detalhadas estão disponíveis no arquivo `dados/fontes_premissas.md`.

### 1.1. Fontes sobre Consumo e Eficiência Energética

Para a análise energética, foram utilizados registros técnicos de luminárias convencionais e LED, além de informações sobre o funcionamento da iluminação pública.

As principais referências foram:

- **Inmetro — Registro nº 006047/2019:** luminária convencional REPUME, modelo DI-960 150W-VS, com potência nominal de 150 W, fluxo luminoso declarado de 13.485 lúmens e eficiência luminosa de 89,9 lm/W.

  Fonte: https://registro.inmetro.gov.br/consulta/detalhe.aspx?pag=1&NumeroRegistro=006047/2019

- **Inmetro — Registro nº 005531/2023:** luminária LED REEME, modelo LD-7P-100-3000-140, com potência nominal de 100 W, fluxo luminoso declarado de 15.000 lúmens e eficiência luminosa de 150 lm/W, conforme a entrada incluída no registro.

  Fonte: https://registro.inmetro.gov.br/consulta/detalhe.aspx?pag=1&NumeroRegistro=005531/2023

- **Inmetro — Registro nº 002951/2023:** reator GOODLUX, modelo SO150EAP26, utilizado como referência para estimar perdas elétricas de 18 W no sistema convencional.

  Fonte: https://registro.inmetro.gov.br/consulta/detalhe.aspx?NumeroRegistro=002951%2F2023&pag=2

- **ANEEL — Resolução Homologatória nº 2.590/2019:** referência para o tempo médio diário de funcionamento da iluminação pública em Osasco, correspondente a 11 horas e 26 minutos.

  Fonte: https://leis.org/institucionais/br/aneel/lei/resolucao-homologatoria/2019/2590/resolucao-homologatoria-n-2590-2019-homologar-o-tempo-por-municipio-a-ser-considerado-para-o-consumo-diario-para-fins-de-faturamento-da-energia-eletrica-destinada-a-iluminacao-publica-e-a-iluminacao-de-vias-internas-de-condominios-conforme

Com base nessas informações, foram considerados dez pontos de iluminação e um funcionamento mensal estimado de 343 horas.

### 1.2. Fontes sobre Energia Solar Fotovoltaica

Para fundamentar a alternativa solar, foram consultadas referências sobre disponibilidade de radiação solar, funcionamento dos sistemas fotovoltaicos e armazenamento de energia.

As principais fontes utilizadas foram:

- **Fundação Instituto Tecnológico de Osasco (FITO, 2020):** Memorial Descritivo e Termo de Referência, contendo dados de irradiação solar atribuídos ao CRESESB e utilizados para estimar a disponibilidade solar em Osasco.

  Fonte: https://fito.edu.br/wp-content/uploads/2020/11/ANEXO-I-TERMO-DE-REFER%C3%8ANCIA-E-MEMORIAL-DESCRITIVO-UNIDADE-ZONA-NORTE-PDF.pdf

- **Departamento de Energia dos Estados Unidos:** informações sobre o funcionamento dos sistemas fotovoltaicos, incluindo painéis, inversores e armazenamento de energia.

  Fonte: https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics

- **Governo Australiano — Your Home:** informações sobre capacidade nominal, capacidade utilizável, profundidade de descarga e eficiência das baterias.

  Fonte: https://www.yourhome.gov.au/energy/batteries

Para a simulação, foram adotadas 2,97 horas de sol pico por dia, correspondentes à média de irradiação horizontal de junho apresentada no estudo da FITO.

Também foram considerados um sistema fotovoltaico de 6,5 kWp, aproveitamento global de 70% e capacidade nominal de armazenamento de 20,48 kWh.

O aproveitamento de 70%, a profundidade de descarga de 80% e a eficiência de saída de 95% representam premissas estabelecidas pela equipe, não resultados de medições.

### 1.3. Fontes sobre Custos

Os custos foram estimados a partir de tarifas oficiais, referências de preços comerciais e premissas orçamentárias definidas pela equipe.

As principais referências foram:

- **Enel Distribuição São Paulo:** tabela tarifária de iluminação pública B4a, associada à Resolução Homologatória ANEEL nº 3.596/2026. Foi adotada uma tarifa de referência de R$ 0,43416/kWh.

  Fonte: https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html

- **Prefeitura de Seringueiras (RO):** Ata de Registro de Preços nº 54/2026, utilizada como referência para o preço de R$ 904,83 de uma luminária REEME da linha LD-7P/100.

  Fonte: https://www.diariomunicipal.com.br/arom/materia/312DE731

- **Excelência Luminárias:** referência comercial de R$ 994,48 para uma luminária pública LED de 100 W com características semelhantes às do equipamento selecionado.

  Fonte: https://excelencialuminarias.com.br/luminaria-comercial-industrial-e-publica/luminaria-publica/luminaria-ornamental/

- **Minha Casa Solar:** painel solar Canadian de 650 W, anunciado por R$ 739,00 na consulta utilizada pelo projeto.

  Fonte: https://www.minhacasasolar.com.br/painel-solar-monocristalino-650w-halfcell-bifacial-canadian-82960

- **Alumifix Energia:** bateria de lítio Gospower de 5,12 kWh, utilizada como referência de preço de R$ 7.160,00.

  Fonte: https://www.alumifixenergia.com.br/collections/sistemas-all-in-one/products/bateria-litio-gospower-5-12-kwh-51-2v-100ah-gaveta

Com base nessas referências, foram estimados investimentos iniciais de R$ 12.500,00 para a alternativa LED conectada à rede e R$ 63.030,00 para a alternativa solar fotovoltaica.

Os valores de instalação, estruturas, equipamentos de conversão e controle e manutenção foram definidos como premissas orçamentárias da equipe.

Os preços comerciais foram utilizados como referências de novembro de 2026 e não representam orçamentos definitivos.

### 1.4. Outras Referências

Também foram consideradas iniciativas reais de modernização da iluminação pública, utilizadas para contextualizar o projeto.

- **Prefeitura de Osasco:** informações sobre a modernização da iluminação pública e a utilização de luminárias LED em espaços públicos.

  Fonte: https://osasco.sp.gov.br/osasco-avanca-em-modernizacao-do-sistema-de-iluminacao-publica/

- **Enel:** projeto de eficiência energética relacionado à modernização da iluminação pública.

  Fonte: https://www.peeenel.com.br/projeto/599

- **REEME:** exemplo de aplicação da linha LD-7P em um projeto de iluminação pública em Itaquaquecetuba.

  Fonte: https://reeme.com.br/case/case-pontos-de-iluminacao-em-itaquaquecetuba/

- **Prefeitura de Curitiba:** exemplo de utilização de energia solar na iluminação do Parque Barigui.

  Fonte: https://www.curitiba.pr.gov.br/noticias/curitiba-testa-energia-solar-na-iluminacao-do-parque-barigui/17271

- **Prefeitura de São Paulo:** exemplo de substituição de iluminação convencional por LED em praça pública.

  Fonte: https://prefeitura.sp.gov.br/web/se/w/noticias/26675

Essas referências demonstram a aplicação das tecnologias estudadas em espaços públicos, mas não comprovam, por si só, a viabilidade da implantação proposta.

## 2. Limitações da Proposta

### 2.1. Utilização de Dados Estimados

O projeto considera uma praça comunitária hipotética localizada em Osasco, São Paulo, com dez pontos de iluminação.

Como não foram realizadas medições presenciais, os dados de consumo, geração solar e custos foram calculados a partir de referências técnicas e premissas estabelecidas pela equipe.

O funcionamento mensal de 343 horas foi definido a partir de uma referência regulatória, considerando meses padronizados de 30 dias.

Dessa forma, os resultados permitem comparar as alternativas em condições semelhantes, mas não representam o consumo real de uma praça existente.

### 2.2. Limitações Técnicas

A implantação das alternativas dependeria de uma avaliação das condições físicas e elétricas do local.

Embora as luminárias selecionadas apresentem características luminosas próximas, não foi realizado um estudo luminotécnico para verificar a distribuição da luz, a uniformidade da iluminação e a adequação dos equipamentos à praça.

Na alternativa solar, a geração de energia pode variar conforme a incidência solar, as condições climáticas, o sombreamento, a temperatura e a orientação dos painéis.

O armazenamento também apresenta limitações, pois a capacidade estimada das baterias não garante autonomia durante vários dias consecutivos de baixa geração solar.

Além disso, seria necessário verificar a compatibilidade elétrica entre painéis, baterias, equipamentos de conversão e luminárias antes de uma instalação real.

### 2.3. Limitações Econômicas

Os custos apresentados representam estimativas preliminares e podem variar conforme os fornecedores, a disponibilidade dos equipamentos, a mão de obra e as condições de instalação.

A alternativa LED conectada à rede apresenta investimento inicial estimado de R$ 12.500,00, enquanto a alternativa solar exige aproximadamente R$ 63.030,00.

A análise também considera reservas mensais estimadas de manutenção de R$ 30,00 para o sistema convencional, R$ 20,00 para o LED conectado à rede e R$ 120,00 para o sistema solar.

Esses valores não correspondem a contratos reais de manutenção.

Também não foram considerados todos os custos futuros de substituição de equipamentos, especialmente baterias e inversores, nem tributos e encargos adicionais na tarifa de energia.

Portanto, a economia de eletricidade não garante, isoladamente, que uma alternativa apresente o melhor retorno financeiro.

### 2.4. Limitações Ambientais

A utilização de luminárias LED pode reduzir o consumo de eletricidade em comparação com o sistema convencional.

A alternativa fotovoltaica também pode diminuir a dependência da energia fornecida pela rede elétrica, utilizando uma fonte renovável.

Entretanto, os benefícios ambientais dependem do desempenho real dos equipamentos, das condições de geração solar e da vida útil dos componentes.

Além disso, a fabricação, o transporte, a manutenção e o descarte de luminárias, painéis solares e baterias também apresentam impactos ambientais.

Esses impactos não foram quantificados no projeto, que concentra sua análise no consumo energético, nos custos estimados e na utilização de energia renovável.

### 2.5. Limitações do Dashboard

O dashboard foi desenvolvido em Python e utiliza os dados organizados no arquivo `dados/consumo_energetico.csv`, juntamente com as funções implementadas em `dashboard/calculos.py`.

O programa apresenta no terminal os resultados dos cálculos e os indicadores utilizados para comparar as três alternativas de iluminação.

Entre as informações apresentadas estão:

- Consumo mensal de energia elétrica.
- Economia de energia em kWh e em percentual.
- Custos mensais estimados de eletricidade.
- Geração solar estimada.
- Capacidade de armazenamento de energia.
- Indicadores de sustentabilidade e participação de energia renovável.
- Comparação dos benefícios das alternativas.

O dashboard não possui interface gráfica, gráficos interativos ou integração com sensores e equipamentos reais.

Também não realiza monitoramento em tempo real. Todos os resultados dependem dos dados e das premissas utilizados na simulação.

## 3. Considerações sobre os Resultados

A análise energética indica que o sistema convencional apresenta consumo estimado de 576,24 kWh por mês, enquanto as alternativas LED apresentam demanda de 343,00 kWh mensais.

A substituição da iluminação convencional por LED representa uma economia estimada de 233,24 kWh por mês, equivalente a aproximadamente 40,48%.

Na alternativa solar fotovoltaica, a geração útil estimada é de 13,51 kWh por dia, considerando um sistema de 6,5 kWp, disponibilidade solar de 2,97 horas de sol pico e aproveitamento global de 70%.

Essa geração é superior à demanda diária estimada das luminárias LED, de aproximadamente 11,43 kWh, nas condições adotadas.

Entretanto, a geração solar pode variar ao longo do ano, e a capacidade de armazenamento prevista não garante o funcionamento contínuo em todas as condições climáticas.

Os resultados demonstram o potencial de redução do consumo energético e de utilização de fontes renováveis na iluminação de espaços públicos.

Contudo, representam projeções baseadas nas premissas do projeto e não garantem o mesmo desempenho em uma instalação real.

Para uma eventual implantação, seriam necessários levantamentos locais, estudos técnicos, dimensionamento dos equipamentos e orçamento detalhado.
