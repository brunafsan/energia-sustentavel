
# Fontes de Dados e Premissas

## 1. Objetivo

Este documento tem como objetivo apresentar as fontes de dados e as premissas utilizadas na análise energética do projeto Iluminação Sustentável para Praças Comunitárias.
Como o estudo considera uma praça hipotética, serão utilizados dados de fontes confiáveis e estimativas justificadas para definir as características dos sistemas de iluminação convencional, LED e solar fotovoltaica.
Essas informações servirão como base para os cálculos de consumo de energia, custos de funcionamento e comparação das alternativas, garantindo maior transparência e coerência aos resultados apresentados no dashboard.

## 2. Premissas Adotadas

### 2.1. Características da Praça

Para a realização do estudo, será considerada uma praça comunitária hipotética, localizada em uma região residencial urbana do município de Osasco, em São Paulo, e utilizada pela população para atividades de lazer e convivência.
A escolha de Osasco como município de referência foi fundamentada na disponibilidade de dados oficiais aplicáveis à análise energética e na existência de iniciativas reais de modernização da iluminação pública. Segundo a Prefeitura de Osasco (2021), o programa Cidade Iluminada já havia instalado 1.009 luminárias decorativas LED em praças, parques e áreas externas de prédios públicos até a data da publicação. Além disso, o município foi beneficiado por um projeto de eficiência energética da Enel voltado à substituição de sistemas convencionais de iluminação pública por luminárias LED.
Essas iniciativas demonstram a aplicação de tecnologias mais eficientes no município e justificam sua utilização como referência para o estudo, embora a praça analisada seja hipotética.
Como premissa inicial, a praça contará com 10 pontos de iluminação, cada um equipado com uma luminária convencional alimentada pela rede elétrica. Essa quantidade foi adotada para fins de simulação, permitindo estimar o consumo energético e comparar as alternativas propostas.
Nos três cenários analisados, será mantida a mesma quantidade de pontos de iluminação, buscando atender a necessidades equivalentes de iluminação.
A quantidade de energia elétrica consumida será estimada em kWh, considerando a potência das luminárias, a quantidade de equipamentos e o tempo de funcionamento. Os resultados serão apresentados na análise energética, com base nas premissas adotadas e nas informações técnicas consultadas.

**fontes:**
https://osasco.sp.gov.br/osasco-avanca-em-modernizacao-do-sistema-de-iluminacao-publica/

https://www.peeenel.com.br/projeto/599

### 2.2. Funcionamento da Iluminação

Para a análise energética, será considerado que o sistema de iluminação da praça funcionará durante o período noturno, com acionamento ao anoitecer e desligamento ao amanhecer.
De acordo com a Resolução Homologatória nº 2.590/2019 da Agência Nacional de Energia Elétrica (ANEEL), o município de Osasco possui um tempo médio diário de referência de 11 horas e 26 minutos para a estimativa do consumo de energia elétrica da iluminação pública.
Com base nesse valor, será considerado um período de 30 dias por mês, totalizando 343 horas mensais de funcionamento.
O mesmo tempo de funcionamento será adotado nos três cenários analisados, permitindo comparar o consumo energético da iluminação convencional, das luminárias LED conectadas à rede elétrica e das luminárias LED alimentadas por energia solar fotovoltaica.
O tempo utilizado representa uma referência regulatória para estimativas de faturamento, não uma medição real da praça hipotética. O funcionamento efetivo poderá variar conforme as condições locais e a época do ano.

**fonte:**

https://leis.org/institucionais/br/aneel/lei/resolucao-homologatoria/2019/2590/resolucao-homologatoria-n-2590-2019-homologar-o-tempo-por-municipio-a-ser-considerado-para-o-consumo-diario-para-fins-de-faturamento-da-energia-eletrica-destinada-a-iluminacao-publica-e-a-iluminacao-de-vias-internas-de-condominios-conforme?termo=RESOLU%C3%87%C3%83O%20HOMOLOGAT%C3%93RIA%20N%C2%BA%202.590%2C%20DE%2013%20DE%20AGOSTO%20DE%202019

### 2.3. Características dos Equipamentos

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

**Fontes:**

**Potência, fluxo e eficiência da luminária LED:** 
https://registro.inmetro.gov.br/consulta/detalhe.aspx?pag=1&NumeroRegistro=005531/2023

**Potência, fluxo e eficiência da luminária convencional:** 
https://registro.inmetro.gov.br/consulta/detalhe.aspx?pag=1&NumeroRegistro=006047/2019

**Uso da linha LD-7P em iluminação pública:**
https://reeme.com.br/case/case-pontos-de-iluminacao-em-itaquaquecetuba/

**Exemplo real de iluminação pública alimentada por energia solar:**
https://www.curitiba.pr.gov.br/noticias/curitiba-testa-energia-solar-na-iluminacao-do-parque-barigui/17271

**Uso real de vapor de sódio e LED em praça pública:**
https://prefeitura.sp.gov.br/web/se/w/noticias/26675

### 2.4. Condições de Geração Solar

Para a alternativa de iluminação solar fotovoltaica, será considerado um sistema capaz de gerar energia elétrica durante o dia e armazená-la em baterias para alimentar as luminárias durante o período noturno.

**Disponibilidade Solar**
A estimativa de geração fotovoltaica será baseada nas condições de radiação solar do município de Osasco, em São Paulo. Como referência, será utilizado o Memorial Descritivo e Termo de Referência da Fundação Instituto Tecnológico de Osasco (FITO, 2020), que apresenta estimativas de geração fotovoltaica elaboradas com dados de radiação solar atribuídos ao CRESESB.
A partir da tabela de irradiação global horizontal apresentada na página 18 do documento, foi calculada uma média anual aproximada de 3,95 kWh/m²/dia, considerando o total anual de 1.442,9 kWh/m² dividido por 365 dias.
Para junho, mês com menor irradiação global horizontal na tabela consultada, o valor corresponde a aproximadamente 2,97 kWh/m²/dia, calculado a partir de 89,1 kWh/m² divididos pelos 30 dias do mês.
Para a simulação, será adotado o valor aproximado de 2,97 horas de sol pico por dia, utilizando a irradiação horizontal como referência simplificada de disponibilidade solar reduzida. Essa escolha busca avaliar a capacidade do sistema fotovoltaico de atender à demanda energética da praça em condições médias menos favoráveis do que a média anual.
Os valores representam estimativas de irradiação para a região, não medições realizadas na praça hipotética. A geração efetiva também dependerá da orientação e inclinação dos painéis, das condições meteorológicas e das características da instalação.

**Perdas Energéticas**
Para os cálculos, será adotado um fator global de aproveitamento de 70%, equivalente a uma estimativa de perdas de 30% no percurso da geração fotovoltaica até o fornecimento da energia às luminárias.
Esse percentual foi definido como premissa do projeto para representar, de maneira simplificada, possíveis perdas relacionadas à temperatura dos painéis, sujeira, sombreamento, cabeamento, armazenamento e conversão elétrica.
A escolha considera a necessidade de incorporar perdas à simulação, conforme os princípios técnicos de funcionamento dos sistemas fotovoltaicos e de armazenamento apresentados pelo Departamento de Energia dos Estados Unidos e pelo Governo Australiano.
O aproveitamento de 70% não corresponde a uma eficiência medida ou especificada pelas fontes consultadas, sendo uma hipótese de cálculo adotada pela equipe para avaliar a solução proposta.

**Geração e Armazenamento de Energia**
Considerando as 10 luminárias LED de 100 W e o funcionamento diário de 11 horas e 26 minutos, a demanda energética estimada será de aproximadamente 11,43 kWh por noite.
Como pré-dimensionamento, será considerado um sistema fotovoltaico com potência instalada de 6,5 kWp. Essa potência foi escolhida para atender à demanda energética prevista e oferecer uma margem de geração no cenário de disponibilidade solar reduzida adotado.
Com 2,97 horas de sol pico por dia e aproveitamento global de 70%, a geração útil estimada será de aproximadamente 13,51 kWh por dia, superior à demanda noturna calculada.
Para o armazenamento, será considerada uma capacidade nominal de 20,48 kWh, correspondente a quatro baterias de lítio de 5,12 kWh. Serão adotadas como premissas uma profundidade de descarga de 80% e uma eficiência de conversão de saída de 95%.
A escolha da capacidade de armazenamento foi fundamentada na necessidade de fornecer energia suficiente para uma noite de funcionamento, considerando uma margem sobre o consumo previsto.
Nessas condições, a energia disponível para alimentar as luminárias será estimada em aproximadamente 15,56 kWh, superior à demanda noturna de 11,43 kWh. A verificação da capacidade útil das baterias será realizada separadamente da estimativa de geração, sem descontar novamente as mesmas perdas já consideradas no fator global de aproveitamento.

**Inversor e Controle de Energia**
Para a conversão e o gerenciamento da energia elétrica, será considerada a utilização de um inversor compatível com o sistema fotovoltaico proposto, capaz de atender à demanda simultânea de 1 kW das luminárias.
Como premissa do projeto, o conjunto de conversão e controle deverá permitir o aproveitamento dos 6,5 kWp de potência fotovoltaica instalada e o gerenciamento da energia armazenada nas baterias.
A escolha de não definir um modelo comercial específico considera o caráter conceitual da proposta, que busca avaliar a viabilidade energética por meio de estimativas e simulações, sem desenvolver um projeto executivo de instalação.
Em uma implantação real, seria necessário selecionar equipamentos compatíveis com as tensões, correntes e características elétricas dos painéis e das baterias.

**Condições da Estimativa**
Os valores apresentados representam premissas e estimativas utilizadas para a simulação energética, não constituindo um projeto executivo de instalação.
A geração calculada considera condições médias de disponibilidade solar reduzida, não garantindo que a mesma quantidade de energia seja produzida diariamente.
Uma eventual implantação dependeria da avaliação das condições locais, das características dos equipamentos, da área disponível para instalação dos painéis e da autonomia necessária durante períodos prolongados de baixa geração solar.
Também seria necessário avaliar a eficiência dos equipamentos de conversão e controle, além de confirmar a compatibilidade elétrica entre os componentes, considerando que ainda não foi definido um modelo comercial específico para o sistema. 

**fontes:**
**Na seção Battery specifications, a página explica capacidade nominal, capacidade utilizável, profundidade de descarga e eficiência das baterias.
Utilizaremos essa fonte para fundamentar os conceitos, deixando os percentuais escolhidos como premissas do projeto.:**
https://www.yourhome.gov.au/energy/batteries

**Essa página explica o funcionamento dos componentes de sistemas fotovoltaicos, incluindo inversores e baterias para utilização da energia durante a noite. Não determina o fator de aproveitamento de 70% escolhido para nossa simulação:**
https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics

**Essa fonte sustenta os dados de irradiação solar apresentados no texto. Trata-se de um estudo técnico de 2020, não de medição atual da praça:**
https://fito.edu.br/wp-content/uploads/2020/11/ANEXO-I-TERMO-DE-REFER%C3%8ANCIA-E-MEMORIAL-DESCRITIVO-UNIDADE-ZONA-NORTE-PDF.pdf

### 2.5. Custos e Tarifas

Para estimar os custos das alternativas de iluminação, serão considerados os investimentos necessários para implantação, os gastos mensais de energia elétrica e as despesas previstas com manutenção.
A análise utilizará tarifas oficiais, preços comerciais de referência e premissas orçamentárias adotadas pela equipe. Como o projeto considera uma praça hipotética, os valores representam estimativas para comparação dos cenários, não orçamentos definitivos de implantação.

**Tarifa de Energia Elétrica**
Para estimar os custos de eletricidade, será utilizada como referência a tarifa de iluminação pública B4a da Enel Distribuição São Paulo, concessionária responsável pelo fornecimento de energia elétrica no município de Osasco.
A escolha dessa classificação considera que a praça hipotética representa um espaço público municipal, com sistema de iluminação de responsabilidade do poder público e alimentado em baixa tensão pela rede de distribuição.
Segundo a tabela tarifária da Enel, estabelecida pela Resolução Homologatória ANEEL nº 3.596/2026, válida a partir de 4 de julho de 2026, a tarifa B4a apresenta os seguintes valores:
- Tarifa de Uso do Sistema de Distribuição (TUSD): R$ 0,25983/kWh.
- Tarifa de Energia (TE): R$ 0,17433/kWh.
- Tarifa total de referência: R$ 0,43416/kWh.

A soma desses componentes será utilizada para estimar o custo mensal de eletricidade dos sistemas convencional e LED conectados à rede elétrica, sem considerar tributos, bandeiras tarifárias ou outros encargos adicionais.

**Custos de Implantação**
Para a estimativa de implantação, será considerado que a praça já possui 10 pontos de iluminação, postes e infraestrutura elétrica básica. Assim, os custos serão direcionados à substituição ou adaptação dos equipamentos necessários em cada alternativa.
No sistema convencional, não será considerado investimento inicial, pois ele representa a situação existente utilizada como referência para a comparação.

**Alternativa 1: Iluminação LED conectada à rede elétrica**
Para a substituição das luminárias convencionais, será adotado um custo estimado de R$ 1.000 por luminária LED de 100 W, totalizando R$ 10.000 para os 10 pontos de iluminação.
A escolha desse valor foi fundamentada em referências de preços de equipamentos semelhantes à luminária REEME selecionada para a análise energética.
Como primeira referência, foi consultada a Ata de Registro de Preços nº 54/2026 da Prefeitura de Seringueiras (RO), publicada no Diário Oficial dos Municípios de Rondônia em 27 de outubro de 2026. O documento apresenta o valor unitário de R$ 904,83 para uma luminária REEME da linha LD-7P/100, em uma contratação que prevê 120 unidades, sem identificar a configuração completa do modelo.
Também foi consultado o preço comercial de R$ 994,48 de uma luminária pública ornamental LED de 100 W, temperatura de cor de 3.000 K, proteção IP66 e eficiência luminosa de 140 lm/W, disponibilizada pela Excelência Luminárias.
Com base nessas referências, foi adotado o valor arredondado de R$ 1.000 por unidade como premissa orçamentária, considerando uma margem em relação aos preços pesquisados.
A estimativa não representa uma cotação exata da luminária REEME LD-7P-100-3000-140. Os preços podem variar conforme o fornecedor, a quantidade adquirida, as características específicas do equipamento e as condições comerciais.
Também será considerada uma despesa estimada de R$ 2.500 com mão de obra e adequações elétricas. Esse valor representa uma premissa orçamentária equivalente a R$ 250 por ponto de iluminação, considerando o aproveitamento da infraestrutura existente.
Dessa forma, o investimento inicial estimado para a alternativa LED será de R$ 12.500.

**Alternativa 2: Iluminação LED alimentada por energia solar fotovoltaica**
Para a alternativa solar, serão consideradas as mesmas 10 luminárias LED de 100 W, além de um conjunto fotovoltaico de 6,5 kWp, baterias para armazenamento e equipamentos necessários ao controle e à conversão de energia.
O orçamento preliminar utilizará os seguintes valores:

|Componente | Quantidade | Valor unitário | Total |
|---|---|---|---|
|Luminárias LED de 100 W | 10 | R$ 1.000,00 | R$ 10.000,00 |
|Painéis solares de 650 W | 10 | R$ 739,00 | R$ 7.390,00 
|Baterias de lítio de 5,12 kWh | 4 | R$ 7.160,00 | R$ 28.640,00 |
|Conjunto de conversão e controle de energia | 1 conjunto | R$ 6.000,00 | R$ 6.000,00 |
|Estrturas cabeamento e proteções | 1 conjunto |  R$ 6.000,00 | R$ 6.000,00 |
|Instalação e adequações do sistema solar | 1 serviço | R$ 5.000,00 | R$ 5.000,00 |
|**Investimento total estimado** | | | R$ 63.030,00

Os preços dos painéis solares e das baterias foram obtidos em páginas comerciais consultadas em novembro de 2026. Esses valores representam referências de mercado e podem variar conforme a disponibilidade, as condições de pagamento e o fornecedor.
O painel solar Canadian de 650 W utilizado como referência estava anunciado por R$ 739,00, mas indisponível em estoque na consulta realizada. Por isso, seu preço será utilizado apenas como referência de orçamento, sem representar uma oferta de fornecimento imediato.
Os valores de R$ 6.000 para o conjunto de conversão e controle de energia, R$ 6.000 para estruturas, cabeamento e proteções e R$ 5.000 para instalação e adequações foram definidos como premissas orçamentárias da equipe.
Para o conjunto de conversão e controle, a estimativa de R$ 6.000 busca representar os custos dos equipamentos necessários ao gerenciamento da geração fotovoltaica, ao carregamento das baterias e ao fornecimento de energia às luminárias.
A escolha de não definir um modelo comercial específico considera o caráter conceitual do projeto. O conjunto deverá ser capaz de atender à demanda simultânea de 1 kW das luminárias e permitir a utilização dos 6,5 kWp de painéis solares e das baterias previstas, mediante dimensionamento compatível.
O valor adotado não corresponde à cotação de um equipamento específico e poderá variar conforme a configuração e as características técnicas necessárias para uma implantação real.
As demais estimativas orçamentárias buscam representar as despesas de montagem, conexão, proteção e instalação do sistema, incluindo as luminárias. Entretanto, não foram obtidas por meio de cotações de serviços ou levantamento detalhado de materiais.
A escolha das quantidades foi fundamentada no pré-dimensionamento energético apresentado na seção 3.4. Os dez painéis de 650 W totalizam 6,5 kWp, enquanto as quatro baterias de 5,12 kWh oferecem capacidade nominal de 20,48 kWh.
A compatibilidade elétrica entre os componentes, incluindo tensões, correntes, equipamentos de controle e eficiência de conversão, dependeria de verificação técnica antes de uma eventual implantação.

**Custos de Operação**
Os custos mensais de eletricidade serão estimados considerando a potência dos equipamentos, a quantidade de luminárias, o funcionamento de 343 horas mensais e a tarifa B4a adotada.
No sistema convencional, será considerada uma potência de 150 W por lâmpada, acrescida de 18 W de perdas estimadas do reator, totalizando 168 W por ponto de iluminação.
O valor de 18 W tem como referência a perda máxima declarada de um reator GOODLUX, modelo SO150EAP26, destinado a lâmpadas de vapor de sódio de 150 W e registrado no Inmetro sob o nº 002951/2023.
Sua utilização representa uma premissa técnica para a simulação, não uma medição do reator da luminária REPUME selecionada. A estimativa considera que essas perdas não estejam incluídas na potência nominal de 150 W adotada para a lâmpada.
Com 10 pontos de iluminação, o consumo mensal estimado do sistema convencional será de 576,24 kWh, correspondente a aproximadamente R$ 250,18 em eletricidade.
Na alternativa LED conectada à rede, serão consideradas 10 luminárias de 100 W, resultando em consumo mensal de 343 kWh e custo estimado de R$ 148,92.
Para a alternativa solar fotovoltaica isolada, será considerado custo nulo de compra de eletricidade da rede, desde que o sistema consiga atender integralmente à demanda energética nas condições simuladas.
Essa condição não significa ausência de consumo elétrico ou de despesas operacionais, pois a energia continuará sendo utilizada pelas luminárias e o sistema exigirá manutenção.

**Custos de Manutenção**
Para representar os gastos recorrentes, serão adotadas reservas mensais preliminares de:
- R$ 30 para o sistema convencional.
- R$ 20 para a iluminação LED conectada à rede.
- R$ 120 para o sistema solar fotovoltaico.

Esses valores representam premissas orçamentárias estabelecidas pela equipe para comparação dos cenários, não preços obtidos em contratos reais de manutenção.
A menor reserva prevista para a alternativa LED considera a expectativa de menor necessidade de substituições de componentes em relação ao sistema convencional. Já a reserva mais elevada para o sistema solar considera a existência de equipamentos adicionais que exigem inspeções e cuidados, como painéis, baterias, conexões e equipamentos de conversão e controle.
As reservas não incluem grandes reparos ou substituições futuras de equipamentos, especialmente baterias e inversores, cujos custos deverão ser reconhecidos como limitações da estimativa.

**Considerações sobre os Custos**
Os valores apresentados constituem estimativas preliminares para avaliar as alternativas de iluminação da praça hipotética.
Os preços comerciais poderão variar ao longo do tempo, e as premissas de instalação e manutenção não substituem cotações profissionais.
A análise econômica completa será desenvolvida na comparação das alternativas, considerando os investimentos iniciais, os custos recorrentes, os benefícios energéticos e as limitações de cada solução.
A redução do consumo de energia da rede não será considerada, isoladamente, como comprovação de maior viabilidade econômica, especialmente na alternativa solar, que exige investimento inicial mais elevado.

**fontes:**

**fundamentar o custo estimado das luminárias LED de 100 W, utilizando o preço registrado de R$ 904,83 para uma luminária REEME da mesma linha e potência:**
https://www.diariomunicipal.com.br/arom/materia/312DE731

**Tarifa B4a de R$ 0,43416/kWh:**
https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html

**Luminária LED comparável: R$ 994,48:**
https://excelencialuminarias.com.br/luminaria-comercial-industrial-e-publica/luminaria-publica/luminaria-ornamental/

**Painel solar Canadian de 650 W: R$ 739,00:**
https://www.minhacasasolar.com.br/painel-solar-monocristalino-650w-halfcell-bifacial-canadian-82960

**Bateria Gospower de 5,12 kWh: R$ 7.160,00:**
https://www.alumifixenergia.com.br/collections/sistemas-all-in-one/products/bateria-litio-gospower-5-12-kwh-51-2v-100ah-gaveta

**Perdas de 18 W do reator GOODLUX:**
https://registro.inmetro.gov.br/consulta/detalhe.aspx?NumeroRegistro=002951%2F2023&pag=2


## 3. Justificativa das Premissas

As premissas adotadas no projeto foram definidas considerando as características de uma praça comunitária hipotética, a disponibilidade de informações técnicas verificáveis e a necessidade de comparar alternativas de iluminação em condições semelhantes.

**Características da Praça e Funcionamento**
A escolha do município de Osasco foi fundamentada na disponibilidade de referências locais sobre modernização da iluminação pública, incluindo iniciativas da Prefeitura de Osasco e projetos de eficiência energética da Enel.
A quantidade de 10 pontos de iluminação foi definida como premissa para representar uma praça comunitária de maneira simplificada, permitindo realizar os cálculos de consumo e custos sem depender de medições de um espaço real.
O tempo de funcionamento de 11 horas e 26 minutos por dia foi adotado com base na referência estabelecida pela Resolução Homologatória ANEEL nº 2.590/2019 para o município de Osasco. Para os cálculos mensais, foi considerado um período padronizado de 30 dias, correspondente a 343 horas de funcionamento.
Esses valores serão mantidos nos três cenários para permitir uma comparação energética sob as mesmas condições de operação.
Características dos Equipamentos
As luminárias convencionais e LED foram selecionadas a partir de modelos reais com informações técnicas disponíveis nos registros do Inmetro.
Para o sistema convencional, foi adotada uma luminária de vapor de sódio de 150 W, com acréscimo estimado de 18 W de perdas do reator. Esse valor foi utilizado como referência técnica para representar o consumo adicional necessário ao funcionamento da lâmpada.
Nas alternativas LED conectada à rede e solar fotovoltaica, será utilizada a mesma luminária de 100 W. Essa escolha permite comparar as fontes de alimentação elétrica sem alterar a potência e as características do equipamento de iluminação entre as duas alternativas.
A utilização de modelos com características luminosas próximas busca estabelecer uma comparação energética inicial, embora a equivalência efetiva da iluminação dependa de uma avaliação luminotécnica.

**Geração Solar e Armazenamento**
Para estimar a disponibilidade solar, foram utilizados os dados de irradiação apresentados no Memorial Descritivo da Fundação Instituto Tecnológico de Osasco (FITO, 2020).
Embora a média anual calculada a partir da tabela seja de aproximadamente 3,95 kWh/m²/dia, foi adotado o valor de 2,97 horas de sol pico por dia, correspondente à média de irradiação horizontal de junho, mês com menor valor na tabela consultada.
Essa escolha busca avaliar a geração fotovoltaica em um cenário mensal de menor disponibilidade solar, evitando dimensionar a solução apenas com base na média anual.
O fator global de aproveitamento de 70% foi definido como premissa para representar, de maneira simplificada, possíveis perdas associadas à geração, ao armazenamento e à conversão de energia.
A potência fotovoltaica de 6,5 kWp, correspondente a 10 painéis de 650 W, foi adotada porque proporciona uma geração útil estimada de 13,51 kWh por dia nas condições simuladas, superior à demanda noturna de aproximadamente 11,43 kWh.
Para o armazenamento, foram consideradas quatro baterias de 5,12 kWh, totalizando 20,48 kWh de capacidade nominal. A profundidade de descarga de 80% e a eficiência de saída de 95% foram estabelecidas como premissas para estimar uma capacidade útil de 15,56 kWh, suficiente para uma noite de funcionamento nas condições previstas.
A capacidade útil das baterias foi verificada separadamente da geração diária, sem aplicar novamente ao cálculo de geração perdas já representadas pelo fator global de aproveitamento.
Para o gerenciamento da energia, foi prevista a utilização de um conjunto de conversão e controle compatível com os painéis, as baterias e a demanda das luminárias. A escolha de não definir um modelo comercial específico considera o caráter conceitual do projeto.

**Custos e Tarifas**
Para estimar as despesas com eletricidade, foi adotada a tarifa de iluminação pública B4a da Enel Distribuição São Paulo, considerando a praça hipotética como um espaço público municipal alimentado em baixa tensão.
O valor de R$ 0,43416/kWh foi obtido na tabela tarifária vigente a partir de julho de 2026 e aplicado igualmente aos sistemas convencional e LED conectados à rede.
Os investimentos iniciais foram estimados a partir de preços comerciais, registros de preços públicos e premissas orçamentárias da equipe.
O custo de R$ 1.000 por luminária LED foi adotado como valor arredondado, considerando a referência de R$ 904,83 para uma luminária REEME da mesma linha e potência e o preço comercial de R$ 994,48 de uma luminária com características semelhantes.
Os custos dos painéis solares e das baterias foram definidos com base em valores anunciados por fornecedores, enquanto as despesas de instalação, estruturas, proteções e conjunto de conversão e controle foram estimadas pela equipe.
Também foram adotadas reservas mensais de manutenção para representar os gastos recorrentes dos três sistemas. Esses valores permitem realizar uma comparação econômica preliminar, sem substituir orçamentos ou contratos de manutenção.
Dessa forma, as premissas buscam estabelecer condições de comparação coerentes com o objetivo do estudo, mantendo identificados os valores provenientes de fontes consultadas e aqueles definidos especificamente para a simulação.


## 4. Limitações dos Dados

O projeto utiliza dados técnicos de fontes consultadas e premissas estabelecidas pela equipe para analisar uma praça comunitária hipotética. Portanto, os resultados representam estimativas de consumo, geração de energia e custos, não medições realizadas em uma instalação existente.

**Ausência de Medições Reais**
Como a praça analisada é hipotética, não foram realizados levantamentos presenciais para verificar a quantidade necessária de luminárias, o consumo elétrico efetivo, as condições dos postes e da infraestrutura ou as características físicas do local.
A quantidade de 10 pontos de iluminação foi definida para a simulação e poderá não corresponder às necessidades de uma praça real.
O tempo diário de 11 horas e 26 minutos representa uma referência regulatória de funcionamento, não uma medição local. Além disso, a adoção de meses padronizados de 30 dias simplifica os cálculos, sem representar exatamente a duração de todos os meses do ano.

**Desempenho dos Equipamentos**
As potências, os fluxos luminosos e as eficiências utilizados foram obtidos de registros técnicos dos equipamentos selecionados.
Entretanto, os valores declarados pelos fabricantes não substituem medições de desempenho em campo. No sistema convencional, as perdas de 18 W do reator foram estimadas a partir de um modelo de referência, não do equipamento efetivamente instalado na luminária escolhida.
Embora as luminárias convencional e LED apresentem fluxos luminosos próximos, não foi realizado um estudo luminotécnico para verificar a distribuição da luz, a iluminância, a uniformidade e o atendimento às necessidades reais de iluminação da praça.
Dessa forma, a comparação considera principalmente o consumo energético, sem comprovar que os diferentes equipamentos produziriam condições equivalentes de iluminação em uma instalação real.

**Condições de Geração Solar**
Os dados de irradiação foram obtidos de um estudo técnico de 2020 referente ao município de Osasco, não de medições realizadas no local hipotético.
O valor de 2,97 horas de sol pico representa uma aproximação baseada na média de irradiação horizontal de junho, não a menor disponibilidade solar possível em um dia específico.
A geração real poderá variar conforme as condições meteorológicas, a temperatura, a orientação e a inclinação dos painéis, o sombreamento, a sujeira e as características da instalação.
O fator global de aproveitamento de 70% foi adotado como premissa simplificada e não corresponde ao desempenho medido de um conjunto específico de equipamentos.
Assim, a geração útil estimada de 13,51 kWh por dia não garante que o sistema consiga atender à demanda em todos os dias do ano, especialmente durante períodos consecutivos de baixa irradiação.

**Armazenamento e Compatibilidade Elétrica**
A capacidade nominal de 20,48 kWh das baterias foi estimada a partir de quatro equipamentos de 5,12 kWh. Entretanto, os percentuais de profundidade de descarga de 80% e eficiência de saída de 95% foram definidos como premissas, sem avaliação prática do conjunto.
A energia efetivamente disponível dependerá das características das baterias, da temperatura, das condições de operação e da eficiência dos equipamentos de conversão.
Também não foi selecionado um modelo comercial específico para o conjunto de conversão e controle. Portanto, ainda seria necessário verificar a compatibilidade entre painéis, baterias, equipamentos de controle e luminárias, considerando tensões, correntes e demais requisitos técnicos.
A área disponível para instalação dos painéis, as estruturas de suporte e a autonomia necessária durante períodos prolongados de baixa geração também dependeriam de avaliação local.

**Custos e Viabilidade Econômica**
Os preços comerciais utilizados representam valores de referência consultados em novembro de 2026, sujeitos a alterações conforme fornecedor, disponibilidade, quantidade adquirida e condições de pagamento.
O preço das luminárias LED foi estimado a partir de equipamentos semelhantes e de um registro de preços públicos, sem obtenção de cotação exata para a configuração completa do modelo REEME selecionado.
Além disso, o painel solar de 650 W utilizado como referência estava indisponível em estoque na consulta realizada.
Os valores atribuídos às estruturas, aos equipamentos de conversão e controle, às instalações e às reservas mensais de manutenção foram estabelecidos como premissas orçamentárias, sem levantamento detalhado de materiais ou cotações profissionais.
A análise também não contempla tributos, bandeiras tarifárias, outros encargos adicionais, grandes reparos ou substituições futuras de equipamentos, especialmente baterias e inversores.
Na alternativa solar isolada da rede elétrica, o custo nulo de compra de energia representa apenas a ausência de fornecimento pela distribuidora. Isso não significa ausência de consumo energético nem garantia de funcionamento contínuo em condições desfavoráveis.

**Alcance dos Resultados**
As limitações identificadas não impedem a comparação preliminar das alternativas, mas devem ser consideradas na interpretação dos resultados.
O estudo permite estimar diferenças de consumo, custos e necessidades energéticas sob condições padronizadas. Entretanto, não comprova, por si só, a viabilidade técnica, luminotécnica ou econômica de uma implantação real.
Para uma eventual execução, seriam necessários levantamentos locais, dimensionamento elétrico e luminotécnico, confirmação da compatibilidade dos componentes e elaboração de um orçamento detalhado.


## 5. Relação com os Cálculos Energéticos

[Explicar como os dados registrados neste documento serão utilizados nos arquivos de análise energética, comparação das alternativas e no dashboard.]
