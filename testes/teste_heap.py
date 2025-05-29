from estruturas.heap_prioridade import processar_chamadas_prioritarias
import heapq


def test_heap_prioridade():
    chamadas = [
        { "id": 1, "local": "Zona Norte", "severidade": 4, "tipo_vegetacao": "cerrado", "clima": "seco" },
        { "id": 2, "local": "Mata Alta", "severidade": 5, "tipo_vegetacao": "pantanal", "clima": "seco" },
        { "id": 3, "local": "Vila Verde", "severidade": 3, "tipo_vegetacao": "mata_atlantica", "clima": "quente" }
    ]

    heap = processar_chamadas_prioritarias(chamadas)

    # Retira o primeiro item do heap para verificar se é o de maior prioridade
    prioridade_negativa, chamada_topo = heapq.heappop(heap)

    print(f"🧪 Testando chamada com maior prioridade...")
    print(f"ID da chamada prioritária: {chamada_topo['id']}")
    print(f"Prioridade calculada: {-prioridade_negativa:.2f}")

    # Esperado: chamada ID 2, pois 5 * 2.0 = 10.0 (pantanal)
    assert chamada_topo["id"] == 2, "Erro: chamada de maior prioridade incorreta"
    print("✅ Heap de prioridade funcionando corretamente.")


test_heap_prioridade()
