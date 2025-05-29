# Importações de módulos customizados
from estruturas.arvore import exibir_hierarquia
from estruturas.heap_prioridade import processar_chamadas_prioritarias
from estruturas.historico import historico_acoes, status_areas
from estruturas.fila import chamadas_emergencia
from estruturas.grafo import mapa
from utils import atender_chamada

import heapq
import time  # Para simular atraso nas respostas


def menu():
    mostrar_menu = True  # Controla se o menu será exibido na próxima iteração

    while True:
        if mostrar_menu:
            print("\n🔥 === FIREALERT - Central de Combate a Queimadas === 🔥")
            print("1. 🌳 Ver hierarquia das regiões")
            print("2. 🚨 Processar chamadas prioritárias")
            print("3. 📜 Ver histórico de ações")
            print("4. 📍 Ver status das áreas")
            print("0. ❌ Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n🌱 Hierarquia das Regiões:")
            time.sleep(1)
            exibir_hierarquia()

        elif opcao == "2":
            chamadas = chamadas_emergencia()
            fila = processar_chamadas_prioritarias(chamadas)
            print("\n🚨 Atendendo ocorrências por prioridade:")
            time.sleep(1)
            while fila:
                _, chamada = heapq.heappop(fila)
                resultado = atender_chamada(chamada)
                print("\n📦 Ocorrência Atendida:")
                print(f"ID.............: {resultado['ocorrencia_id']}")
                print(f"Prioridade.....: {resultado['prioridade']:.2f}")
                print(f"Rota...........: {' -> '.join(resultado['rota'])}")
                print(f"Tempo Estimado.: {resultado['tempo_estimado']} min")
                print(f"Ações..........: {', '.join(resultado['acao'])}")
                print(f"Status Área....: {resultado['status_area']}")
                time.sleep(1)

        elif opcao == "3":
            print("\n📜 Histórico de Ações:")
            time.sleep(1)
            if historico_acoes:
                for i, acao in enumerate(historico_acoes[::-1], 1):
                    print(f"{i}. {acao}")
            else:
                print("Nenhuma ação registrada ainda.")

        elif opcao == "4":
            print("\n📍 Status das Áreas Monitoradas:")
            time.sleep(1)
            if status_areas:
                for area, status in status_areas.items():
                    print(f"{area}: {status}")
            else:
                print("Nenhuma área registrada ainda.")

        elif opcao == "0":
            print("✅ Sistema encerrado com sucesso.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

        # Pergunta se o usuário deseja ver o menu novamente
        resposta = input("\nDeseja ver o menu novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("✅ Sistema encerrado com sucesso.")
            break
        mostrar_menu = True


if __name__ == "__main__":
    menu()


