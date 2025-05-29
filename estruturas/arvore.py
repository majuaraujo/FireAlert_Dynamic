# Representa a hierarquia das regiões monitoradas
hierarquia = {
    "Estado do Norte Verde": {
        "Município A": ["Zona Norte", "Zona Leste"],
        "Município B": ["Vila Verde", "Mata Alta"]
    }
}


def exibir_hierarquia():
    for estado, municipios in hierarquia.items():
        print(f"🌎 {estado}")
        for municipio, zonas in municipios.items():
            print(f"  🏙️ {municipio}")
            for zona in zonas:
                print(f"    🌲 {zona}")
