from estruturas.grafo import calcular_menor_caminho

# Grafo de teste: locais conectados com tempos de deslocamento
mapa_teste = {
    "Base Central": {"Zona Norte": 10, "Vila Verde": 5},
    "Zona Norte": {"Base Central": 10, "Mata Alta": 7},
    "Vila Verde": {"Base Central": 5, "Mata Alta": 3},
    "Mata Alta": {"Zona Norte": 7, "Vila Verde": 3}
}

# Teste: calcular caminho da base até a Mata Alta
rota, tempo = calcular_menor_caminho(mapa_teste, "Base Central", "Mata Alta")

print("Menor rota:", " -> ".join(rota))
print("Tempo estimado:", tempo)
