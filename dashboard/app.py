
import csv
from pathlib import Path

from calculos import (
    calcular_consumo,
    calcular_consumo_mensal,
    calcular_economia_energetica,
    calcular_economia_percentual,
    calcular_custo_mensal,
    calcular_reducao_custos,
    calcular_participacao_renovavel,
    calcular_geracao_solar,
    calcular_capacidade_util_baterias,
    calcular_saldo_energetico,
    verificar_atendimento_solar,
    calcular_energia_rede,
    calcular_custo_operacional,
    calcular_investimento_total,
    calcular_retorno_simples
)


TARIFA = 0.43416

MANUTENCAO = {
    "atual": 30,
    "alternativa_1": 20,
    "alternativa_2": 120
}

INVESTIMENTOS = {
    "atual": 0,
    "alternativa_1": 12500,
    "alternativa_2": 63030
}

NOMES = {
    "atual": "Iluminacao convencional",
    "alternativa_1": "LED conectado a rede",
    "alternativa_2": "LED solar fotovoltaico"
}

POTENCIA_SOLAR_KWP = 6.5
HORAS_SOL_PICO = 2.97
APROVEITAMENTO_SOLAR = 0.70

CAPACIDADE_BATERIAS = 20.48
PROFUNDIDADE_DESCARGA = 0.80
EFICIENCIA_BATERIAS = 0.95


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def carregar_dados():
    caminho = Path(__file__).resolve().parent.parent / "dados" / "consumo_energetico.csv"

    dados = {}

    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            cenario = linha["cenario"]

            quantidade = int(linha["quantidade"])
            potencia = float(linha["potencia_w"])
            horas = float(linha["horas_dia"])
            dias = int(linha["dias_mes"])

            consumo_diario = calcular_consumo(
                potencia,
                horas,
                quantidade
            )

            consumo_mensal = calcular_consumo_mensal(
                consumo_diario,
                dias
            )

            dados[cenario] = {
                "nome": NOMES[cenario],
                "quantidade": quantidade,
                "potencia": potencia,
                "horas": horas,
                "dias": dias,
                "fonte": linha["fonte_energia"],
                "consumo_diario": consumo_diario,
                "consumo_mensal": consumo_mensal,
                "manutencao": MANUTENCAO[cenario],
                "investimento": INVESTIMENTOS[cenario]
            }

    esperados = {"atual", "alternativa_1", "alternativa_2"}

    if set(dados) != esperados:
        raise ValueError("O CSV deve conter os tres cenarios do projeto.")

    geracao_solar = calcular_geracao_solar(
        POTENCIA_SOLAR_KWP,
        HORAS_SOL_PICO,
        APROVEITAMENTO_SOLAR
    )

    capacidade_util = calcular_capacidade_util_baterias(
        CAPACIDADE_BATERIAS,
        PROFUNDIDADE_DESCARGA,
        EFICIENCIA_BATERIAS
    )

    demanda_solar = dados["alternativa_2"]["consumo_diario"]

    solar_atende = verificar_atendimento_solar(
        geracao_solar,
        capacidade_util,
        demanda_solar
    )

    for cenario, informacoes in dados.items():
        consumo = informacoes["consumo_mensal"]

        if cenario == "alternativa_2":
            energia_renovavel = consumo if solar_atende else 0
        else:
            energia_renovavel = 0

        energia_rede = calcular_energia_rede(
            consumo,
            energia_renovavel
        )

        custo_eletricidade = calcular_custo_mensal(
            energia_rede,
            TARIFA
        )

        custo_operacional = calcular_custo_operacional(
            custo_eletricidade,
            informacoes["manutencao"]
        )

        participacao = calcular_participacao_renovavel(
            energia_renovavel,
            consumo
        )

        informacoes["energia_rede"] = energia_rede
        informacoes["energia_renovavel"] = energia_renovavel
        informacoes["custo_eletricidade"] = custo_eletricidade
        informacoes["custo_operacional"] = custo_operacional
        informacoes["participacao_renovavel"] = participacao

    dados["solar"] = {
        "geracao_diaria": geracao_solar,
        "capacidade_util": capacidade_util,
        "saldo_diario": calcular_saldo_energetico(
            geracao_solar,
            demanda_solar
        ),
        "atende": solar_atende
    }

    return dados


def apresentar_projeto():
    print("\n" + "=" * 60)
    print("DASHBOARD DE ENERGIA SUSTENTAVEL")
    print("Iluminacao Sustentavel para Pracas Comunitarias")
    print("=" * 60)

    print("\nProjeto: Global Solution 2026")
    print("Local: Praca comunitaria hipotetica em Osasco - SP")
    print("Quantidade: 10 pontos de iluminacao")

    print("\nObjetivo:")
    print("Comparar alternativas de iluminacao considerando")
    print("consumo energetico, custos e sustentabilidade.")


def apresentar_consumo(dados):
    print("\n" + "=" * 60)
    print("1. CONSUMO DE ENERGIA")
    print("=" * 60)

    for cenario in NOMES:
        item = dados[cenario]

        print(f"\n{item['nome']}")
        print(f"Potencia por luminaria: {item['potencia']:.0f} W")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Consumo diario: {item['consumo_diario']:.2f} kWh")
        print(f"Consumo mensal: {item['consumo_mensal']:.2f} kWh")


def apresentar_comparacao(dados):
    print("\n" + "=" * 60)
    print("2. COMPARACAO DAS ALTERNATIVAS")
    print("=" * 60)

    atual = dados["atual"]
    led = dados["alternativa_1"]
    solar = dados["alternativa_2"]

    economia = calcular_economia_energetica(
        atual["consumo_mensal"],
        led["consumo_mensal"]
    )

    percentual = calcular_economia_percentual(
        atual["consumo_mensal"],
        led["consumo_mensal"]
    )

    print(f"\nEconomia com luminarias LED: {economia:.2f} kWh/mes")
    print(f"Reducao do consumo: {percentual:.2f}%")

    for item in (atual, led, solar):
        print(f"\n{item['nome']}")
        print(f"Eletricidade: {formatar_moeda(item['custo_eletricidade'])}/mes")
        print(f"Manutencao: {formatar_moeda(item['manutencao'])}/mes")
        print(f"Custo operacional: {formatar_moeda(item['custo_operacional'])}/mes")
        print(f"Investimento: {formatar_moeda(item['investimento'])}")

    print("\nEconomia mensal de eletricidade em relacao ao atual:")

    for item in (led, solar):
        economia_custo = calcular_reducao_custos(
            atual["custo_eletricidade"],
            item["custo_eletricidade"]
        )

        print(f"{item['nome']}: {formatar_moeda(economia_custo)}")


def apresentar_indicadores(dados):
    print("\n" + "=" * 60)
    print("3. INDICADORES DE SUSTENTABILIDADE")
    print("=" * 60)

    atual = dados["atual"]

    for cenario in NOMES:
        item = dados[cenario]

        economia = calcular_economia_percentual(
            atual["consumo_mensal"],
            item["consumo_mensal"]
        )

        print(f"\n{item['nome']}")
        print(f"Consumo: {item['consumo_mensal']:.2f} kWh/mes")
        print(f"Reducao energetica: {economia:.2f}%")
        print(f"Energia da rede: {item['energia_rede']:.2f} kWh/mes")
        print(f"Participacao renovavel propria: {item['participacao_renovavel']:.2f}%")
        print(f"Custo operacional: {formatar_moeda(item['custo_operacional'])}/mes")

    solar = dados["solar"]

    print("\nIndicadores do sistema fotovoltaico:")
    print(f"Geracao diaria estimada: {solar['geracao_diaria']:.2f} kWh")
    print(f"Capacidade util das baterias: {solar['capacidade_util']:.2f} kWh")
    print(f"Saldo diario estimado: {solar['saldo_diario']:.2f} kWh")

    if solar["atende"]:
        print("Atendimento solar: suficiente nas condicoes simuladas")
    else:
        print("Atendimento solar: nao comprovado nas condicoes simuladas")


def apresentar_beneficios(dados):
    print("\n" + "=" * 60)
    print("4. BENEFICIOS E VIABILIDADE")
    print("=" * 60)

    atual = dados["atual"]

    for cenario in ("alternativa_1", "alternativa_2"):
        item = dados[cenario]

        economia_mensal = calcular_reducao_custos(
            atual["custo_operacional"],
            item["custo_operacional"]
        )

        investimento = calcular_investimento_total(
            [item["investimento"]]
        )

        retorno = calcular_retorno_simples(
            investimento,
            economia_mensal
        )

        print(f"\n{item['nome']}")
        print(f"Economia operacional: {formatar_moeda(economia_mensal)}/mes")

        if retorno is None:
            print("Retorno simples: nao calculavel")
        else:
            print(f"Retorno simples estimado: {retorno:.1f} meses")

    print("\nBeneficios esperados:")
    print("- Reducao do consumo com luminarias LED")
    print("- Menor compra de energia da rede no cenario solar")
    print("- Comparacao dos custos entre as alternativas")
    print("- Apoio a decisoes sobre iluminacao sustentavel")

    print("\nLimitacoes:")
    print("- Os dados representam uma simulacao.")
    print("- A geracao solar depende das condicoes climaticas.")
    print("- Nao foi realizada uma simulacao de varios dias de bateria.")
    print("- O retorno simples nao considera todos os custos futuros.")


def executar_dashboard():
    try:
        dados = carregar_dados()
    except (OSError, ValueError, KeyError) as erro:
        print(f"Erro ao carregar os dados: {erro}")
        return

    apresentar_projeto()
    apresentar_consumo(dados)
    apresentar_comparacao(dados)
    apresentar_indicadores(dados)
    apresentar_beneficios(dados)

    print("\n" + "=" * 60)
    print("FIM DO DASHBOARD")
    print("=" * 60)


if __name__ == "__main__":
    executar_dashboard()
