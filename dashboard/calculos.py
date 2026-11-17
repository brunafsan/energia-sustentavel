
def calcular_consumo(potencia, horas, quantidade):
    return (potencia * horas * quantidade) / 1000


def calcular_consumo_mensal(consumo_diario, dias):
    return consumo_diario * dias


def calcular_economia_energetica(consumo_atual, consumo_alternativa):
    return consumo_atual - consumo_alternativa


def calcular_economia_percentual(consumo_atual, consumo_alternativa):
    if consumo_atual == 0:
        return 0

    return ((consumo_atual - consumo_alternativa) / consumo_atual) * 100


def calcular_custo_mensal(energia_rede, tarifa):
    return energia_rede * tarifa


def calcular_reducao_custos(custo_atual, custo_alternativa):
    return custo_atual - custo_alternativa


def calcular_participacao_renovavel(energia_renovavel, consumo_total):
    if consumo_total == 0:
        return 0

    return min(energia_renovavel, consumo_total) / consumo_total * 100


def calcular_geracao_solar(potencia_kwp, horas_sol_pico, aproveitamento):
    return potencia_kwp * horas_sol_pico * aproveitamento


def calcular_capacidade_util_baterias(capacidade_nominal, profundidade_descarga, eficiencia_saida):
    return capacidade_nominal * profundidade_descarga * eficiencia_saida


def calcular_saldo_energetico(geracao_solar, consumo_diario):
    return geracao_solar - consumo_diario


def verificar_atendimento_solar(geracao_solar, capacidade_util, consumo_diario):
    return geracao_solar >= consumo_diario and capacidade_util >= consumo_diario


def calcular_energia_rede(consumo_total, energia_renovavel):
    return max(0, consumo_total - energia_renovavel)


def calcular_custo_operacional(custo_eletricidade, custo_manutencao):
    return custo_eletricidade + custo_manutencao


def calcular_economia_operacional(custo_atual, custo_alternativa):
    return custo_atual - custo_alternativa


def calcular_investimento_total(custos):
    return sum(custos)


def calcular_retorno_simples(investimento, economia_mensal):
    if economia_mensal <= 0:
        return None

    return investimento / economia_mensal
