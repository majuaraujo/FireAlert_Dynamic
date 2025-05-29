from utils import calcular_prioridade, atender_chamada

# Mapa de exemplo local para o teste (simula conexões entre pontos)
mapa = {
    "Base Central": {"Zona Norte": 10, "Mata Alta": 12},
    "Zona Norte": {"Mata Alta": 7},
    "Mata Alta": {"Zona Norte": 7}
}

# Teste para calcular_prioridade


def test_calcular_prioridade():
    chamada = {
        "id": 1,
        "local": "Zona Norte",
        "severidade": 4,
        "tipo_vegetacao": "cerrado",
        "clima": "seco"
    }
    prioridade = calcular_prioridade(chamada)
    assert round(prioridade, 2) == 4.8  # 4 * 1.2
    print("✅ Prioridade calculada corretamente.")

# Teste para atender_chamada


def test_atender_chamada():
    chamada = {
        "id": 2,
        "local": "Mata Alta",
        "severidade": 5,
        "tipo_vegetacao": "pantanal",
        "clima": "seco"
    }
    resultado = atender_chamada(chamada)
    assert resultado["ocorrencia_id"] == 2
    assert "Mata Alta" in resultado["rota"]
    assert resultado["status_area"] == "controle em andamento"
    print("✅ Atendimento executado com sucesso.")

# Executa os testes
test_calcular_prioridade()
test_atender_chamada()

