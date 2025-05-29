print("==== 🔥 INICIANDO TESTES DO SISTEMA FIREALERT ====\n")

# Teste da árvore
from teste_arvore import test_exibir_hierarquia
test_exibir_hierarquia()

# Teste da fila
from teste_fila import test_chamadas_emergencia
test_chamadas_emergencia()

# Teste do grafo
from estruturas.grafo import calcular_menor_caminho


def test_grafo():
    print("🛣️ Testando cálculo de menor caminho...")
    mapa_teste = {
        "Base Central": {"Zona Norte": 10, "Vila Verde": 5},
        "Zona Norte": {"Base Central": 10, "Mata Alta": 7},
        "Vila Verde": {"Base Central": 5, "Mata Alta": 3},
        "Mata Alta": {"Zona Norte": 7, "Vila Verde": 3}
    }
    rota, tempo = calcular_menor_caminho(mapa_teste, "Base Central", "Mata Alta")
    assert rota == ["Base Central", "Vila Verde", "Mata Alta"]
    assert tempo == 8
    print(f"✅ Menor rota: {' -> '.join(rota)} (Tempo: {tempo})\n")

test_grafo()

# Teste do heap (prioridade)
from estruturas.heap_prioridade import processar_chamadas_prioritarias
from estruturas.fila import chamadas_emergencia


def test_heap_prioridade():
    print("⚖️ Testando fila de prioridade...")
    chamadas = chamadas_emergencia()
    fila = processar_chamadas_prioritarias(chamadas)
    assert fila[0][1]['id'] == 2  # Prioridade mais alta: severidade 5, vegetação pantanal
    print("✅ Fila de prioridade ordenada corretamente.\n")
test_heap_prioridade()

# Teste do histórico e status das áreas
from estruturas.historico import historico_acoes, status_areas


def test_historico_status():
    print("📚 Testando histórico e status das áreas...")
    historico_acoes.clear()
    status_areas.clear()
    historico_acoes.append("Aplicar barreira de contenção")
    historico_acoes.append("Criar aceiro")
    status_areas["Zona Norte"] = "controle em andamento"
    assert len(historico_acoes) == 2
    assert status_areas["Zona Norte"] == "controle em andamento"
    print("✅ Histórico e status atualizados corretamente.\n")

test_historico_status()

# Teste do atendimento de chamada
from utils import atender_chamada
from estruturas.grafo import mapa


def test_atendimento_utils():
    print("🚨 Testando função de atendimento de chamada...")
    chamada = {
        "id": 1,
        "local": "Zona Norte",
        "severidade": 4,
        "tipo_vegetacao": "cerrado",
        "clima": "seco"
    }
    resultado = atender_chamada(chamada)
    assert resultado['prioridade'] == 4 * 1.2
    assert resultado['status_area'] == "controle em andamento"
    assert "Aplicar barreira de contenção" in resultado['acao']
    print("✅ Atendimento processado com sucesso.\n")

test_atendimento_utils()

print("🎉 TODOS OS TESTES FORAM EXECUTADOS COM SUCESSO.")

