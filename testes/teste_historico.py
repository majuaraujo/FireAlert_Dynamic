from estruturas.historico import historico_acoes, status_areas


def test_pilha_acoes():
    # Limpa a pilha antes do teste
    historico_acoes.clear()

    # Simula ações
    historico_acoes.append("Criar aceiro")
    historico_acoes.append("Barreira de contenção")

    print("📦 Testando pilha de ações...")
    assert historico_acoes[-1] == "Barreira de contenção", "Erro: ação no topo da pilha incorreta"
    assert len(historico_acoes) == 2, "Erro: número de ações incorreto"
    print("✅ Pilha de ações funcionando corretamente.")


def test_status_areas():
    # Limpa e define novo status
    status_areas.clear()
    status_areas["Zona Norte"] = "controle em andamento"

    print("🗺️ Testando status das áreas...")
    assert status_areas["Zona Norte"] == "controle em andamento", "Erro: status da área incorreto"
    print("✅ Lista de status funcionando corretamente.")


test_pilha_acoes()
test_status_areas()
