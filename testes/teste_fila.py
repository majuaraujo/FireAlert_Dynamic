from estruturas.fila import chamadas_emergencia


def test_chamadas_emergencia():
    print("📞 Testando fila de chamadas...")

    chamadas = chamadas_emergencia()

    # Verifica se há 3 chamadas
    assert len(chamadas) == 3

    # Verifica se a primeira chamada é da Zona Norte
    assert chamadas[0]["local"] == "Zona Norte"

    print("✅ Fila de chamadas funcionando corretamente.\n")

test_chamadas_emergencia()
