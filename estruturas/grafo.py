import heapq

# Retorna o menor caminho e custo entre origem e destino usando Dijkstra.


def calcular_menor_caminho(grafo, origem, destino):
    fila_prioridade = [(0, origem, [])]  # (custo acumulado, local atual, caminho)
    visitados = set()

    while fila_prioridade:
        custo, atual, caminho = heapq.heappop(fila_prioridade)

        if atual in visitados:
            continue

        caminho = caminho + [atual]
        visitados.add(atual)

        if atual == destino:
            return caminho, custo

        for vizinho, distancia in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo + distancia, vizinho, caminho))

    return [], float('inf')  # Caso não haja caminho possível

# Mapa
mapa = {
    "Base Central": {"Zona Norte": 10, "Vila Verde": 5},
    "Zona Norte": {"Base Central": 10, "Mata Alta": 7},
    "Vila Verde": {"Base Central": 5, "Mata Alta": 3},
    "Mata Alta": {"Zona Norte": 7, "Vila Verde": 3}
}


