from estruturas.grafo import calcular_menor_caminho
from estruturas.historico import historico_acoes, status_areas

# Pesos por tipo de vegetação
peso_vegetacao = {
    "cerrado": 1.2,
    "mata_atlantica": 1.5,
    "pantanal": 2.0
}


def calcular_prioridade(chamada):
    tipo = chamada['tipo_vegetacao']
    severidade = chamada['severidade']
    return severidade * peso_vegetacao.get(tipo, 1.0)


def atender_chamada(chamada):
    from estruturas.grafo import mapa  # importa localmente para evitar dependência externa

    prioridade = calcular_prioridade(chamada)
    rota, tempo = calcular_menor_caminho(mapa, "Base Central", chamada['local'])

    acoes = ["Aplicar barreira de contenção", "Criar aceiro"]
    for acao in acoes:
        historico_acoes.append(acao)

    status_areas[chamada['local']] = "controle em andamento"

    return {
        "ocorrencia_id": chamada['id'],
        "prioridade": prioridade,
        "acao": acoes,
        "rota": rota,
        "tempo_estimado": tempo,
        "status_area": status_areas[chamada['local']]
    }
